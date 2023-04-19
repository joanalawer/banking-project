from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, ValidationError, DateField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from main.models import Customer

class NewAccount(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(30)])
    othername = StringField('Other Name(s)', validators=[Length(30)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(30)])
    email = StringField('Email Address', validators=[DataRequired(), Length(35), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired(), Length(max=200)])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Register')

    print(firstname, othername, lastname, email, password, confirm_password, address, phone_number)
    
    def validate_email(self, field):
        if Customer.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    
    def validate_username(self, field):
        if Customer.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class CustomerLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters long')])
    # remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

    def validate_on_submit(self):
        return super().validate_on_submit()

    def validate_username(self, field):
        username = Customer.query.filter_by(username=field.data).first()
        if username is None:
            raise ValidationError('Invalid username')

    def validate_password(self, field):
        password = Customer.query.filter_by(password=field.data).first()
        if password is None:
            raise ValidationError('Invalid password')


# class Balance(FlaskForm):
#     confirm_pin = StringField('PIN', validators=[DataRequired])

# class Deposit(FlaskForm):
#     acc_number = StringField('Account Number', validators=[DataRequired()])
#     amount = StringField('Amount', validators=[DataRequired()])
#     pin = StringField('PIN', validators=[DataRequired])

# class Withdrawal(FlaskForm):
#     acc_number = StringField('Account Number', validators=[DataRequired()])
#     amount = StringField('Amount', validators=[DataRequired()])
#     pin = StringField('PIN', validators=[DataRequired])

# class Transfer(FlaskForm):
#     acc_number = StringField('Account Number', validators=[DataRequired()])
#     target_account = StringField('Target Account', validators=[DataRequired()])
#     amount = StringField('Amount', validators=[DataRequired()])
#     pin = StringField('PIN', validators=[DataRequired])

# class Statement(FlaskForm):
#     acc_number = StringField('Account Number', validators=[DataRequired()])
#     start_date = DateField('Start Date', validators=[DataRequired])
#     start_date = DateField('Start Date', validators=[DataRequired])
#     pin = StringField('PIN', validators=[DataRequired])