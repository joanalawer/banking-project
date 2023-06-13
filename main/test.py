from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user
from your_app import app, db
from your_app.models import User
from your_app.forms import CustomerLoginForm

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if current_user.is_authenticated:
        return redirect(url_for('user_page'))

    form = CustomerLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if not user:
            flash("There's no account with the username!")
            return redirect(url_for('login_user'))

        if not user.check_password(password):
            flash("Invalid username and password combination.")
            return redirect(url_for('login_user'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        return redirect(next_page or url_for('user_page'))

    return render_template('login.html', form=form)
