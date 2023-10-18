import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('PERIBANK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()