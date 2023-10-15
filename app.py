from flask_migrate import Migrate
from sys import exit
from decouple import config
from os import environ
from config import config_dict
from __init__ import create_app, db
# WARNING: Don't run with debug turned on in production! ... change default = False
DEVELOPMENT = config('development', default=True, cast=bool)

# The configuration
get_config_mode = 'development' if DEVELOPMENT else 'production'
# Uncomment below line if you wish to use all the three
# get_config_mode = 'development' if DEVELOPMENT else 'production' if DEVELOPMENT =='production' else 'testing'

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [development, testing, production] ')

app = create_app(app_config)
Migrate(app, db)

if DEVELOPMENT:
    app.logger.info('DEBUG       = ' + str(DEVELOPMENT))
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DB_URL        = ' + app_config.SQLALCHEMY_DATABASE_URI)

if __name__ == '__main__':
    app.run(debug=True)         #debug-True' automatically detects changes and updtaes the application with no need to rerun.
    






