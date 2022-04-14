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


#------------------------------------------------------
# Register the blueprints
#------------------------------------------------------
def _registerBlueprints(flask_app: flask.Flask):
    flask_app.register_blueprint(routes.bp_test, url_prefix='/test')
    

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


app = flask.Flask(__name__)
app_config = _getConfigurationClass(app.env)
_setConfigurations(app, app_config)
_registerBlueprints(app)


