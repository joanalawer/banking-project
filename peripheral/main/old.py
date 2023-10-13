import os
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import LoginManager, login_required,login_user, logout_user, current_user
from main import blueprint, forms
from main.forms import CustomerLogin
from main.banker import *
 
@blueprint.route('/login-user', methods=["GET", "POST"])
def login_user():
    if current_user.is_authenticated:
        return redirect(url_for('user_page'))

    form = CustomerLogin()
    if form.validate_on_submit():
        customer_login = request.form
        username = customer_login.get('username', "")
        password = customer_login.get('password', "")

        user = Users.query.filter_by(username=username.data).first()
        # Check if username exists & if login details match
        check_username_password = check_if_username_matches_password(username, password)
        
        if check_username_password == "Username does not exist":
            flash("There's no account with the username!")
            return render_template('login.html', error="There's no account with the username!")
        
        if check_username_password is False:
            flash("Invalid username and password combination.")
            return render_template('login.html', error="Invalid username and password combination.")
  
        # if user and user.check_password(password=password.data):
        login_user(user, form.remember_me.data) 
        return redirect(request.args.get('next') or url_for('user_page'))
        # flash('Invalid username/password combination')
        # return redirect(url_for('bankers.login'))
    
    return render_template('login.html', form=form)