from re import L
from flask import Flask, request, Response
from flask_migrate import Migrate
from flask_restful import wraps
from flask_cors import CORS
import os, json
from threading import Thread
from functools import wraps
import requests
from models import db

f = open('data.json')
conf = json.load("conf.json")
f.close()

API_KEY = conf["FILE_API_KEY"]
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

def get_chunk(filename, byte1=None, byte2=None):
    filesize = os.path.getsize(filename)
    yielded = 0
    yield_size = 1024 * 1024

    if byte1 is not None:
        if not byte2:
            byte2 = filesize
        yielded = byte1
        filesize = byte2

    with open(filename, 'rb') as f:
        content = f.read()

    while True:
        remaining = filesize - yielded
        if yielded == filesize:
            break
        if remaining >= yield_size:
            yield content[yielded:yielded+yield_size]
            yielded += yield_size
        else:
            yield content[yielded:yielded+remaining]
            yielded += remaining


@api.route("/upload", methods = ["POST"])
def upload():
    if request.json.get("APIKEY", None) == API_KEY:
        folder = request.json.get("folder", None)
        size = request.json.get("size", None)
        file = request.json.get("file", None)
        with f.open("/storage/"+folder+"/s"+size+".mp4", "w") as fil:
            fil.write(file)
        return ({"floc":"/storage"+folder+"/s" + size + ".mp4"}), 200
    return 401

"""
HELPERS
"""
if __name__ == "__main__":
    api.run(debug=True, host="0.0.0.0", port=80)