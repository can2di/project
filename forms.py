from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    user = StringField('user', validators=[validators.DataRequired()])
    password = StringField('password', validators=[validators.DataRequired()]) 

    submit = SubmitField('Submit')

class TransactionForm(FlaskForm):
    type = SelectField('Type', choices=[('Expense', 'Expense'), ('Income', 'Income')], validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired(), Length(min=1, max=10)])  
    category = StringField('Category', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])  
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')