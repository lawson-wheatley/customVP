from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, jwt_required
from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
import hashlib, os, json

api = Flask(__name__)
api.config["JWT_SECRET_KEY"] = "adfs0a9sdf9aklm"
api.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=6)

f = open('data.json')
conf = json.load("conf.json")
f.close()

API_KEY = conf["API_KEY"]
from models import User, SubUser

@api.route("/login", methods = ["POST"])
def login():
    user = request.json.get("id", None)
    password = request.json.get("password", None)
    key = request.json.get("APIKEY", None)
    usr = User.query.filter(User.email == user).first()
    if usr and key == API_KEY and (usr.password == checkPass(password, usr.salt)):
        access_token = create_access_token(identity = id)
        response = jsonify(access_token=access_token)
        return response
    return 401
    
@api.route("/register", methods = ["POST"])
def register():
    username = request.json.get("username", None)
    email = request.json.get("email", None).lower()
    password = request.json.get("password", None)
    user = User.query.filter(User.email == email).first()
    if user:
        return jsonify({"message":"Email already in use"}), 400
    passthesalt = hashPass(password=password)
    user = User(displayName = displayName, username = username, email = email, password=passthesalt[1], salt = passthesalt[0])
    db.session.add(user)
    db.session.commit()
    return create_token(email, password)

@api.route("/createsubuser", methods = ["POST"])
@jwt_required()
def createuser():
    if request.json.get("APIKEY", None) == API_KEY:
        usr = get_jwt_identity()
        sub = SubUser(hasPin = request.json.get("hasPin", False), pin = request.json.get("pin", None), usr = usr, access = request.json.get("access"))
        db.session.add(sub)
        usr.subUsers.insert(sub)
        db.session.commit()
        return jsonify ({"Message":"SubUser Created"}), 200

@api.route("/verify/user", methods = ["POST"])
@jwt_required()
def verify():
    if request.json.get("APIKEY", None) == API_KEY:
        usr = get_jwt_identity()
        return jsonify({"message":"verified login", "id":usr}), 200
    return jsonify({"message":"NOT VERIFIED"}), 401

@api.route("/verify/subuser", methods = ["POST"])
@jwt_required()
def verify():
    if request.json.get("APIKEY", None) == API_KEY:
        usr = get_jwt_identity()
        sub = SubUser.filter.query(SubUser.usr == usr).first()
        if sub:
            return jsonify({"message":"verified subuser", "id":sub}), 200
    return jsonify({"message":"NOT VERIFIED"}), 401

@api.route("/verify/subuser/pin", methods = ["POST"])
@jwt_required()
def verify():
    if request.json.get("APIKEY", None) == API_KEY:
        usr = get_jwt_identity()
        sub = SubUser.filter.query(SubUser.usr == usr).first()
        if sub:
            if not sub.hasPin or request.json.get("pin") == sub.pin:
                return jsonify({"message":"Verified", "id":sub.id, "pin":sub.pin}), 200
    return jsonify({"message":"NOT VERIFIED"}), 401

@api.route("/verify/subuser/access", methods = ["POST"])
@jwt_required()
def verify():
    if request.json.get("APIKEY", None) == API_KEY:
        usr = get_jwt_identity()
        sub = SubUser.filter.query(SubUser.usr == usr).first()
        if sub:
            return jsonify({"canaccess": request.json.get("accesslevel", None) == sub.access}), 200
    return jsonify({"canaccess":"false"}), 401

@api.after_request
def refresh_expiring_jwt(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(hours = 3))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity = get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        return response

"""
Helpers
"""
def create_token(email, password):
    user = User.query.filter(User.email==email).first()
    if checkPass(password, user.salt) != user.password:
        return {"msg":"incorrect email or password"}, 401
    access_token = create_access_token(identity = user.id)
    response = jsonify(access_token=access_token, ppic=user.picture)
    return response

def hashPass(password : str):
    salt = str(os.urandom(32))
    key = hashlib.pbkdf2_hmac('sha256', password.encode("UTF-8"), salt.encode(), 1000, dklen=128)
    return (salt, key)
    
def checkPass(password : str, salt: str) -> str:
    return hashlib.pbkdf2_hmac('sha256', password.encode("UTF-8"), salt.encode(), 1000, dklen=128)

