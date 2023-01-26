import os
from flask import Flask, render_template, request, url_for, redirect 
# from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required,login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from config import Config
# from forms import NewAccount
from init_db import configure_database
from models import Customer

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)           # Instance of the flask web application
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'test_customers.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# app.config.from_object(Config)
configure_database(app)

db = SQLAlchemy(app)
# bootstrap = Bootstrap(app)
login_manager = LoginManager()
# login_manager = LoginManager(app)
login_manager.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    form = request.form

    # form = NewAccount(request.POST)
    if form.validate_on_submit():
        firstname = form.firstname.data
        othername = form.othername.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        address = form.address.data
        phone = form.phone_number.data
        acc_number = ''
        check = check_if_user_exist(email)
        if check == False:
            customer = {
                "firstname" : firstname,
                "othername" : othername,
                "lastname" : lastname,
                "email" : email,
                "password" : password,
                "address" : address,
                "phone" : phone,
                "acc_number" : acc_number
            }
            db.session.add(customer)
            db.session.commit()
            return redirect(url_for('profile'))
        else:
            return render_template('register.html')
    return render_template('register.html', form=form)

def check_if_user_exist(email):
    user = Customer.query.filter_by(email=email).first()
    if user:
        return "Customer already exists!"
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
  
@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/cash_bank')
def cash_bank():
    return render_template('cash_bank.html')

@app.route('/digital')
def digital():
    return render_template('digital.html')

@app.route('/crypto')
def crypto():
    return render_template('crypto.html')

if __name__ == '__main__':
    app.run(debug=True)         #debug-True' automatically detects changes and updtaes the application with no need to rerun.