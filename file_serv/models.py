from flask_sqlalchemy import Model
import sqlalchemy
from sqlalchemy import DateTime, ForeignKey, databases, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = sqlalchemy()

class Video(db.Model):
    __tablename__ = "video"
    id = db.Column(Integer, primary_key = True)
    title = db.Column(String, nullable = False)
    access = db.Column(Integer, nullable = False)
