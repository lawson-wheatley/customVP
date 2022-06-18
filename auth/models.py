from flask_sqlalchemy import Model
import sqlalchemy
from sqlalchemy import ForeignKey, databases, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = sqlalchemy()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(Integer, primary_key = True)
    username = db.Column(String(40), unique=True, nullable=False)
    email = db.Column(String(80), unique=True, nullable=False)
    password = db.Column(String(128), unique=False, nullable=False)
    salt = db.Column(String(32), unique=False, nullable=False)
    subUsers = db.relationship("subUser")

class SubUser(db.Model):
    __tablename__ = "subUser"
    ppic = db.Column(String, nullable = False)
    hasPin = db.Column(Boolean, nullable = False)
    pin = db.Column(Boolean, nullable = True)
    name = db.Column(String(40), nullable=False)
    access = db.Column(Integer, nullable = False)
    usr = db.Column(Integer, ForeignKey("user.id"))

