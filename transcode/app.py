from re import L
from flask import Flask, request, Response
from flask_migrate import Migrate
from flask_restful import wraps
from flask_cors import CORS
import os, json
from threading import Thread
from functools import wraps
import requests
import re, subprocess
import ffmpeg


f = open('data.json')
conf = json.load("conf.json")
f.close()

API_KEY = conf["FILE_API_KEY"]
api = Flask(__name__)

def verification_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        auth_token = request.headers.get("AuthToken", "")
        response = requests.post(f"{conf['AUTH_SERVER']}/verify/user", headers={'AuthToken': auth_token}, json={"APIKEY":conf["AUTH_API_KEY"]})
        if id:=response.json.get('id'):
            func(id, *args, **kwargs)
        else:
            return 401


@api.route("/upload", methods = ["POST"])
def upload():
    if request.json.get("APIKEY", None) == API_KEY:
        folder = request.json.get("folder", None)
        file = request.json.get("file", None)
        with f.open("/storage/"+folder+"/original.mp4", "w") as fil:
            fil.write(file)
        o = subprocess.check_output(["ffprobe", "-hide_banner", "/storage/"+folder+"/original.mp4"])
        match = re.search(r"Video:.+?(\d+x\d+) \[SAR.+", o)
        v_size = match.group(1)
        
    return 401

"""
HELPERS
"""



if __name__ == "__main__":
    api.run(debug=True, host="0.0.0.0", port=80)