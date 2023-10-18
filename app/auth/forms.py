from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
from models import User

class CustomerLogin(Form):
    email = StringField('Username', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters long')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class RegistrationForm(From):
    