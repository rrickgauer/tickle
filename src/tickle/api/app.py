"""
********************************************************************************************

This is the entry point for running an application.
    - Create a new flask application object
    - Register all the blue prints

********************************************************************************************
"""

from __future__ import annotations
import flask
from . import routes
from tickle.common.config import configs
from tickle.common.config.base import ConfigBase
import pymysql


#------------------------------------------------------
# Register the blueprints
#------------------------------------------------------
def _registerBlueprints(flask_app: flask.Flask):
    # make a new blueprint to add the v1 prefix to the url
    bp_version = flask.Blueprint('version', __name__)

    bp_version.register_blueprint(routes.bp_test, url_prefix='/test')
    bp_version.register_blueprint(routes.bp_watches, url_prefix='/watches')
    bp_version.register_blueprint(routes.bp_internal, url_prefix='/internal')
    bp_version.register_blueprint(routes.bp_search_tickers, url_prefix='/search/tickers')

    flask_app.register_blueprint(bp_version, url_prefix='/v1')
    

#------------------------------------------------------
# Get the configuration class to use for the application
#------------------------------------------------------
def _getConfigurationClass(enviornment) -> ConfigBase:
    if enviornment == "production":
        return configs.Production
    else:
        return configs.Dev

#------------------------------------------------------
# Configure the application
#------------------------------------------------------
def _setConfigurations(flask_app: flask.Flask, selected_config: ConfigBase):
    flask_app.config.from_object(selected_config)
    flask_app.json_encoder = selected_config.JSON_ENCODER

    pymysql.credentials.USER     = selected_config.DB_USER
    pymysql.credentials.PASSWORD = selected_config.DB_PASSWORD
    pymysql.credentials.DATABASE = selected_config.DB_NAME
    pymysql.credentials.HOST     = selected_config.DB_HOST


# Main logic
app = flask.Flask(__name__)
app_config = _getConfigurationClass(app.env)
_registerBlueprints(app)
_setConfigurations(app, app_config)

