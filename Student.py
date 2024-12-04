
from sqlalchemy import Column, Integer, String  # Import String
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import declarative_base

# Base = declarative_base()

db = SQLAlchemy()

class Student(db.Model):  # Inherit from db.Model
    __tablename__ = 'students'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    city = db.Column(String(50), nullable=False)
    addr = db.Column(String(200), nullable=False)
    pin = db.Column(String(10), nullable=False)

    def __repr__(self):
        return f"<Student {self.name}>"

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin