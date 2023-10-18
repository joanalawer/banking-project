from flask import render_template
from main import blueprint
from auth import auth

@blueprint.route('/')
def index():
    return render_template('index.html')

@auth.route('/login')
def login():
    return render_template('auth/login.html')
