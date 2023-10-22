import os
from flask import Flask
from app import create_app, db
from app.models import User
from flask_migrate import Migrate

app = create_app('default')
app = Flask(__name__)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User)

# Unit test launcher command
# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    app.run(debug=True)