from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, Email


class StudentForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])
    city = StringField('City', validators=[validators.DataRequired()])
    addr = StringField('Address', validators=[validators.DataRequired()])
    pin = StringField('PIN', validators=[validators.DataRequired(), validators.Length(min=4, max=10)])  # Add length validation

    submit = SubmitField('Submit')