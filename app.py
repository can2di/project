from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField,validators
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
from views import Controller
from models import db
# from flask_login import LoginManager



app = Flask(__name__)
controller = Controller(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = "random string"
# login_manager = LoginManager(app)  # Initialize LoginManager
# login_manager.login_view = 'login'  # Specify the login view


db.init_app(app)







with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)





