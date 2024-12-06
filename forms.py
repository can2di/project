from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=25)])
    password = PasswordField('Password', validators=[Length(min=4, max=25)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=25)])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField('Register/Login')

class TransactionForm(FlaskForm):
    type = SelectField('Type', choices=[('Expense', 'Expense'), ('Income', 'Income')], validators=[DataRequired()])
    amount = StringField('Amount', validators=[Length(min=1, max=10)])  
    category = StringField('Category', validators=[Length(min=4, max=25)])
    date = StringField('Date', validators=[DataRequired()])  
    description = StringField('Description', validators=[Length(min=1, max=25)])
    submit = SubmitField('Add Transaction')

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[Length(min=1, max=25)])
    submit = SubmitField('Add Category')

class ReportForm(FlaskForm):
    type = SelectField('Filter by Type', choices=[('all', 'All'), ('income', 'Income'), ('expense', 'Expense')])
    submit = SubmitField('Filter By Type')