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

from tickle.common import config

#------------------------------------------------------
# Register the blueprints
#------------------------------------------------------
def _registerBlueprints(flask_app: flask.Flask):
    flask_app.register_blueprint(routes.bp_test, url_prefix='/test')
    
#------------------------------------------------------
# Configure the application
#------------------------------------------------------
def _setConfiguration(flask_app: flask.Flask):
    if flask_app.env == "production":
        selected_config = config.Production
    else:
        selected_config = config.Dev

    flask_app.config.from_object(selected_config)
    flask_app.json_encoder = selected_config.JSON_ENCODER


app = flask.Flask(__name__)


_registerBlueprints(app)
_setConfiguration(app)


