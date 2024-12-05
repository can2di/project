from sqlalchemy import Column, Integer, String  # Import String
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# class User(db.Model):  # Inherit from db.Model
#     __tablename__ = 'users'

#     id = db.Column(Integer, primary_key=True)
#     user = db.Column(String(100), nullable=False)
#     password = db.Column(String(50), nullable=False)
   


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)  # Increased email length
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.id}>"

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)


# class User(db.Model):
#     # ... other fields (username, email, etc.)

#     password_hash = db.Column(db.String(128), nullable=False)

#     def set_password(self, password):
#         """Hashes a password and stores the hash in the password_hash field."""
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         """Checks if a provided password matches the stored hash."""
#         return check_password_hash(self.password_hash, password)

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