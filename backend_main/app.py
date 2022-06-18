from re import L
from ssl import VERIFY_X509_STRICT
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from models import db
from flask import Flask, request, jsonify, make_response, g, send_from_directory
from flask_migrate import Migrate
from flask_restful import Resource, wraps
from flask_cors import CORS
import hashlib, os, uuid, json
from functools import wraps
import requests

f = open('data.json')
conf = json.load("conf.json")
f.close()

api = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
api.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'tmpdb.db')
db.init_app(api)

migrate = Migrate(api, db)
CORS(api)
with api.app_context():
    db.create_all()

from models import User, SubUser, Video, watchedUntil, Title

def verification_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        auth_token = request.headers.get("AuthToken", "")
        response = requests.post(f"{conf['AUTH_SERVER']}/verify/user", headers={'AuthToken': auth_token}, json={"APIKEY":conf["AUTH_API_KEY"]})
        if id:=response.json.get('id'):
            func(id, *args, **kwargs)
        else:
            return 401

def sub_user_verification_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        auth_token = request.headers.get("AuthToken", "")
        if request.method == "GET":
            sub = request.args.get("sub")
            pin = request.args.get("pin")
        else:
            sub = request.json.get("sub", None)
            pin = request.args.get("pin", None)
        response = requests.get(f"{conf['AUTH_SERVER']}/verify/subuser", headers={'AuthToken': auth_token}, json={"APIKEY":conf["AUTH_API_KEY"]})
        if id:=response.json.get('id'):
            func(id, *args, **kwargs)
        else:
            return 401

@api.route("/login", methods = ["POST", "GET"])
def login():
    return requests.post(f"{conf['AUTH_SERVER']}",  json={"id":request.json.get("email", None), "password":request.json.get("password", None), "APIKEY":conf["AUTH_API_KEY"]})

@api.route("/register", methods=["POST","GET"])
def register():
    return requests.post(f"{conf['AUTH_SERVER']}",  json={"id":request.json.get("email", None), "password":request.json.get("password", None), "APIKEY":conf["AUTH_API_KEY"]})

@api.route("/setsub", methods=["POST"])
@verification_required()
def set_subUser(id):
    subUser = request.json.get("sub", None)
    sub = SubUser.query.filter(SubUser.id == subUser).first()
    if not sub:
        return 403
    if sub.usr != id:
        return 403
    if sub.hasPin:
        if sub.pin == int(request.json.get("pin"), None):
            return jsonify({"subUser":sub.id, "pin":sub.pin}), 200
        return 401
    return jsonify({"subUser":sub.id, "pin":sub.pin}), 200

@api.route("/getsubs", methods=["GET"])
@verification_required()
def get_subs(id):
    subs = User.query.filter(User.id == id).first().subUsers
    return jsonify([subUser_to_json(sub) for sub in subs])


genres = ["Romantic Comedy", "Comedy", "Drama", "Action", "Fantasy", "Thriller", "Horror"]
@api.route("/home", methods=["GET"])
@sub_user_verification_required()
def home(id):
    recently_watched = [title_to_json(watched_until_to_title(watch)) for watch in watchedUntil.query.filter(watchedUntil.usr == id).order_by(watchedUntil.lastWatched.desc()).paginate(0, 20, False)]
    return jsonify({"Recently Watched":recently_watched}), 200
    

"""
HELPERS
"""

def watched_until_to_title(watchedUntil):
    return Title.query.filter(Title.id == watchedUntil.title).first()

def title_to_json(title):
    dic = {"id":title.id, "isSeries":title.isSeries, "pic":title.picLocation, "rating":title.rating, "desc":title.desciption}

def subUser_to_json(usr):
    dic = {"hasPin":usr.hasPin, "name":usr.name, "ppic": usr.ppic}
    return dic

if __name__ == "__main__":
    api.run(debug=True, host="0.0.0.0", port=80)