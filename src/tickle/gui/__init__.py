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
from tickle.common import url_converters
from tickle.common.config import configs

#------------------------------------------------------
# Setup the custom url type converters for some enums
#------------------------------------------------------
def _setupCustomConverters(flask_app: flask.Flask):
    flask_app.url_map.converters.update(ticker_type=url_converters.TickerTypeConverter)
    flask_app.url_map.converters.update(watch_type=url_converters.WatchTypeConverter)

#------------------------------------------------------
# Register the blueprints
#------------------------------------------------------
def _registerBlueprints(flask_app: flask.Flask):
    flask_app.register_blueprint(routes.bp_home, url_prefix='/home')


def _additionalConfig(flask_app: flask.Flask):
    flask_app.json_encoder = configs.Production.JSON_ENCODER


# Main logic
app = flask.Flask(__name__)
_setupCustomConverters(app)
_registerBlueprints(app)
_additionalConfig(app)
