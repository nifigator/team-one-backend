import os

import connexion
# import yaml
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
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

# DB_USER = config['db']['user']
# DB_PASSWORD = config['db'].get('password', '')
# DB_NAME = config['db']['base']
# DB_HOST = config['db'].get('host', 'localhost')
# DB_PORT = config['db'].get('port', 5432)

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
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     'postgresql://{user}:{password}@{host}:{port}/{base}'.format(user=DB_USER,
#     password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, base=DB_NAME)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# Initiialize Marshmallow
# ma = Marshmallow(app)

