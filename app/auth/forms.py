from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
from models import User

class CustomerLogin(Form):
    email = StringField('Username', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters long')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class RegistrationForm(Form):
    firstname = StringField('First Name', validators=[DataRequired(), Length(30)])
    othername = StringField('Other Name(s)', validators=[Length(30)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(30)])
    email = StringField('Email Address', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired, Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
                                                                                       'Usernames must have only letters, '
                                                                                       'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired(), Length(max=200)])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')