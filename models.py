from sqlalchemy import Column, Integer, String  # Import String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):  # Inherit from db.Model
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    user = db.Column(String(100), nullable=False)
    password = db.Column(String(50), nullable=False)
   

    def __repr__(self):
        return f"<User {self.user}>"

    def __init__(self, user, password):
        self.user = user
        self.password = password

class Transaction(db.Model):  # Inherit from db.Model
    __tablename__ = 'transactions'

    id = db.Column(Integer, primary_key=True)
    type = db.Column(String(100), nullable=False)
    amount = db.Column(String(100), nullable=False)
    category = db.Column(String(50), nullable=False)
    date = db.Column(String(50), nullable=False)
    description = db.Column(String(50), nullable=False)
   

    def __repr__(self):
        return f"<Transaction {self.type}>"

    def __init__(self, type, amount, category, date, description):
        self.type = type
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def delete(self):
        db.session.delete(self)
        db.session.commit()