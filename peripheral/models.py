from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from __init__ import login_manager, db
import datetime
from sqlalchemy import DateTime

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))
    acc_number = db.Column(db.Integer, unique=True, index=True)
    is_active = db.Column(db.Boolean)
    last_login = db.Column(DateTime, default=datetime.datetime.now )

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]
            setattr(self, property, value)
    def get_id(self):
        return (self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    firstname = db.Column(db.String(64), index=True)
    othername = db.Column(db.String(64),  index=True)
    lastname = db.Column(db.String(64), index=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(64), unique=True, index=True)
    address = db.Column(db.String(128), index=True)
    phone_number = db.Column(db.Integer, unique=True, index=True)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]
            setattr(self, property, value)

@login_manager.user_loader
def load_user(id):
    return Users.query.filter_by(id=id).first()
