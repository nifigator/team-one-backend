import os

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

import connexion
# import yaml
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow

from swagger_ui_bundle import swagger_ui_3_path
options = {'swagger_path': swagger_ui_3_path}

basedir = os.path.abspath(os.path.dirname(__file__))

# config_file = os.path.join(basedir, 'config.yaml')

# def get_config(config_file: str) -> dict:
#     if os.path.exists(config_file):
#         with open(config_file, 'rt') as f:
#             config = yaml.safe_load(f.read())
#         return config
#     return {}
  
# config = get_config(config_file)

DB_USER = os.environ.get('ONE_DB_USER')
DB_PASSWORD = os.environ.get('ONE_DB_PASSWORD')
DB_NAME = os.environ.get('ONE_DB_NAME')
DB_HOST = os.environ.get('ONE_DB_HOST', 'localhost')
DB_PORT = os.environ.get('ONE_DB_PORT', 5432)

# JWT_ISSUER = config['jwt']['issuer']
# JWT_SECRET = config['jwt']['secret']
# JWT_LIFETIME = config['jwt']['lifetime']
# JWT_ALGORITHM = config['jwt']['algorithm']

# Create the connexion application instance
connex_app = connexion.App(__name__, 
                           specification_dir=os.path.join(basedir, 'api'))

# Get the underlying Flask app instance
app = connex_app.app


# Configure the SQLAlchemy part of the app instance
# app.config['SQLALCHEMY_ECHO'] = config.get('sql_echo') or False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://{user}:{password}@{host}:{port}/{base}'.format(user=DB_USER,
    password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, base=DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initiialize Marshmallow
# ma = Marshmallow(app)

