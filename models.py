from sqlalchemy import Column, Integer, String, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager



db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)  # Increased email length
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.id}>"
    
    def get_id(self):
        return str(self.id)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)



class Transaction(db.Model):  # Inherit from db.Model
    __tablename__ = 'transactions'

    id = db.Column(Integer, primary_key=True)
    type = db.Column(String(100), nullable=False)
    amount = db.Column(String(100), nullable=False)
    category = db.Column(String(50), nullable=False)
    # category_id = db.Column(Integer, ForeignKey('categories.id'), nullable=False)
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

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), nullable=False)

    # Define a foreign key relationship with Transaction model
    # transactions = db.relationship('Transaction', backref='category', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Category {self.name}>"