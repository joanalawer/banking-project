
from main.models import Customer, Users
from __init__ import db
from random import randint

def check_if_customer_exist(email):
    try:
        customer = db.session.query(Customer).filter(Customer.email==email).first()
        if customer:
            return "User already available"
        return "User not available"
    except Exception as e:
        return f"Could not check. Got this error: {e}"

def create_account_number():
    # TODO: You can generate your random unique account number from here and return it
    account_number_length = 12
    range_start = 10**(account_number_length-1)
    range_end = (10**account_number_length)-1
    return randint(range_start, range_end)

def save_user_data_to_database(user_data):
    try:
        user = Users(**user_data) # prepare user details to model
        db.session.add(user) # Add user details to model without saving
        db.session.flush() # get added details before saving user details to model
        user_id = user.id # get added user id from model
        db.session.commit() # save user details to model
        return user_id
    except Exception as e:
        return f"User details not saved. Got this error: {e}"

def save_customer_data_to_database(customer_data):
    try:
        db.session.add(Customer(**customer_data))
        db.session.commit()
        return "Customer details saved"
    except Exception as e:
        return f"Customer details not saved. Got this error: {e}"

def check_if_password_matches(password, confirmPassword):
    # You can also hash the password in a new function/method return it to be save in the db
    if password != confirmPassword:
        return False
    return True