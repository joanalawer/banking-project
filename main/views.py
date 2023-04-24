import os
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import LoginManager, login_required,login_user, logout_user, current_user
from main import blueprint, forms
from main.forms import CustomerLogin
from main.banker import *

@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/login')
def login():
    return render_template('login.html')

@blueprint.route('/register')
def register():
    return render_template('register.html')

@blueprint.route('/user_page')
@login_required
def user():
    return render_template('user_page.html')

@blueprint.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@blueprint.route('/cash_bank')
@login_required
def cash_bank():
    return render_template('cash_bank.html')

@blueprint.route('/digital')
@login_required
def digital():
    return render_template('digital.html')

@blueprint.route('/crypto')
@login_required
def crypto():
    return render_template('crypto.html')

@blueprint.route('/register-user', methods=["POST"])
def register_user():
    new_customer = request.form
    firstname = new_customer.get('firstname', "")
    othername = new_customer.get('othername', "")
    lastname = new_customer.get('lastname', "")
    email = new_customer.get('email', "")
    password = new_customer.get('password', "")
    confirmPassword = new_customer.get('confirmPassword', "") 
    cashBank = new_customer.get('cashBank', "")
    digitalBank = new_customer.get('digitalBank', "")
    cryptoBank = new_customer.get('cryptoBank', "")
    address = new_customer.get('address', "")
    phone_number = new_customer.get('phone', "")
    username = lastname + firstname
    
    check_password = check_if_password_matches(password, confirmPassword)# Check if password matches
    if check_password is False:
        flash("Password and confirm password do not match. Try again.")
        return render_template('register.html', error= "Password and confirm password do not match. Try again.") 

    acc_number = create_account_number() # Create account number

    customer_exist = check_if_customer_exist(email) # Check if email exist
    if "error" in customer_exist:
        flash(customer_exist)
        return render_template('register.html', error= customer_exist)  
    if customer_exist == "User already available":
        flash("Customer already exists!")
        return render_template('register.html', error= "Customer already exists!")    
    
    # Get user details in dict format and save it to database
    user_data = {
            "username" : username,
            "password" : password,
            "acc_number" : acc_number,
            "is_active": False
                }
    get_user_id_response = save_user_data_to_database(user_data)
    if "error" in str(get_user_id_response):
        flash(get_user_id_response)
        return render_template('register.html', error= get_user_id_response)

    customer_data = {
            "user_id": get_user_id_response,
            "firstname" : firstname,
            "lastname" : lastname,
            "othername": othername,
            "username": username,
            "email" : email,
            "address" : address,
            "phone_number" : phone_number
                }
    save_customer_response = save_customer_data_to_database(customer_data)
    if "error" in save_customer_response:
        flash(save_customer_response)
        return render_template('register.html', error= save_customer_response)
    flash(save_customer_response)
    return redirect(url_for('bankers.login'))
           
@blueprint.route('/login-user', methods=["POST"])
def login_user():
    if current_user.is_authenticated:
        return redirect(url_for('user_page'))

    customer_login = request.form
    username = customer_login.get('username', "")
    password = customer_login.get('password', "")
    
    # Cgeck if username exists & if login details match
    check_username_password = check_if_username_matches_password(username, password)
    if "error" in check_username_password:
        flash(check_username_password)
        return render_template('login.html', error=check_username_password)
    if check_username_password == "Username does not exist":
        flash("There's no account with username!")
        return render_template('login.html', error="There's no account with the username!")
    if check_username_password is False:
        flash("Invalid username and password combination.")
        return render_template('login.html', error="Invalid username and password combination.")

    form = CustomerLogin()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=username.data).first()
        if user and user.check_password(password=password.data):
            login_user(user, form.remember_me.data) 
            # the user is redirected to either the page they were trying 
            # to access before they were asked to login 
            # (stored in the next query parameter) 
            return redirect(request.args.get('next') or url_for('user_page'))
        flash('Invalid username/password combination')
        return redirect(url_for('bankers.login'))
    return render_template('user_page.html')

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))