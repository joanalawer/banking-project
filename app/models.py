from flask_login import UserMixin   #, login_required
from app import login_manager, db
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    acc_number = db.Column(db.Integer, unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
@property
def password(self):
    raise AttributeError('password is not a readable attribute')

@password.setter
def password(self, password):
	self.password_hash = generate_password_hash(password)
	
def verify_password(self, password):
	return check_password_hash(self.password_hash, password)

def __repr__(self):
	return '<User %r>' % self.username
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Example usage of protecting routes that can only be used by authenticated users
# @app.route('/secret')
# @login_required
# def secret():
#       return 'Only authenticated users are allowed!'

# class Customer(db.Model):
#     __tablename__ = 'customers'
#     id = db.Column(db.Integer, primary_key = True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
#     firstname = db.Column(db.String(64), index=True)
#     othername = db.Column(db.String(64),  index=True)
#     lastname = db.Column(db.String(64), index=True)
#     username = db.Column(db.String(20), nullable=False, unique=True)
#     email = db.Column(db.String(64), unique=True, index=True)
#     address = db.Column(db.String(128), index=True)
#     phone_number = db.Column(db.Integer, unique=True, index=True)

#     def __init__(self, **kwargs):
#         for property, value in kwargs.items():
#             if hasattr(value, '__iter__') and not isinstance(value, str):
#                 value = value[0]
#             setattr(self, property, value)
