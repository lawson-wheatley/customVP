from flask_sqlalchemy import Model
import sqlalchemy
from sqlalchemy import DateTime, ForeignKey, databases, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = sqlalchemy()

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('video_id', db.Integer, db.ForeignKey('title.id'), primary_key=True)
)

class Title(db.Model):
    __tablename__ = "title"
    id = db.Column(Integer, primary_key = True)
    name = db.Column(String, nullable = False)
    isSeries = db.Column(Boolean, nullable = False)
    Videos = db.relationship("video")
    desciption = db.Column(String, nullable = True)
    picLocation = db.Column(String, nullable = False)
    rating = db.Column(Integer, nullable = False)
    access = db.Column(Integer, nullable = False)
    tags = db.relationship('tag', secondary = tags, lazy = True,
        backref=db.backref('pages', lazy=True))

class Video(db.Model):
    __tablename__ = "video"
    id = db.Column(Integer, primary_key = True)
    overarch = db.Column(Integer, ForeignKey("title.id"))
    title = db.Column(String, nullable = False)
    description = db.Column(String, nullable = True)
    flocation = db.Column(String, nullable = False)
    watches = db.Column(Integer, nullable = False, default = 0)
    access = db.Column(Integer, nullable = False)
    watchedUn = db.relationship("watchtime")

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(Integer, primary_key = True)
    subUsers = db.relationship("subUser")

class SubUser(db.Model):
    __tablename__ = "subUser"
    ppic = db.Column(String, nullable = False)
    hasPin = db.Column(Boolean, nullable = False)
    name = db.Column(String(40), nullable=False)
    usr = db.Column(Integer, ForeignKey("user.id"))
    access = db.Column(Integer, nullable = False)

class watchedUntil(db.Model):
    __tablename__ = "watchtime"
    id = db.Column(Integer, primary_key = True)
    lastWatched = db.Column(DateTime, nullable = False)
    time = db.Column(Integer, nullable = False)
    usr = db.Column(Integer, nullable = False)
    video = db.ForeignKey(Video, nullable = False)
    title = db.ForeignKey(Title, nullable = False)

class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(Integer, primary_key = True)
    name = db.Column(String, primary_key = True)
