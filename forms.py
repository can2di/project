from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo


class UserForm(FlaskForm):
    user = StringField('user', validators=[validators.DataRequired()])
    password = StringField('password', validators=[validators.DataRequired()]) 
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class TransactionForm(FlaskForm):
    type = SelectField('Type', choices=[('Expense', 'Expense'), ('Income', 'Income')], validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired(), Length(min=1, max=10)])  
    category = StringField('Category', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])  
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Add Category')