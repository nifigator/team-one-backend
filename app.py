"""
Main module of the server file
"""

# 3rd party modules
import connexion

# Local modules
import config

def dummy(**kwargs):
    return 'Method not yet implemented.', 200

if __name__ == '__main__':
    app = config.connex_app
    # app = connexion.FlaskApp(__name__, specification_dir='api/')
    app.add_api('common.yaml')
    app.run(port=8080)

