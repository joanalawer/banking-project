from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Simulated User and Customer models
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class CustomerLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters long')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

    def validate_username(self, field):
        customer = Customer.query.filter_by(username=field.data).first()
        if customer is None:
            raise ValidationError('Invalid username')

    def validate_password(self, field):
        customer = Customer.query.filter_by(username=self.username.data).first()
        if customer and not customer.check_password(field.data):
            raise ValidationError('Invalid password')

    def validate_on_submit(self):
        if not super(CustomerLogin, self).validate_on_submit():
            return False
        
        customer = Customer.query.filter_by(username=self.username.data).first()
        if not customer or not customer.check_password(self.password.data):
            raise ValidationError('Invalid username or password')

        return True

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = CustomerLogin()

    if form.validate_on_submit():
        # Simulated authentication logic
        user = User(form.username.data, form.password.data)
        if user.check_password(form.password.data):
            # Successful login
            return redirect(url_for('success'))
        else:
            # Invalid credentials
            form.username.errors.append('Invalid username or password')
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == '__main__':
    app.run()
