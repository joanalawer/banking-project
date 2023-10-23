from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from app import db
from auth import auth
from models import User
from forms import CustomerLogin, RegistrationForm

# Function to check user(email & password)) in db when login form is submitted"
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = CustomerLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

# Function to logout user after login"
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

# Function to add new user to db when registration form is submitted"
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)