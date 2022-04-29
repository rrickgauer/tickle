"""
********************************************************************************************

This is the entry point for running an application.
    - Create a new flask application object
    - Register all the blue prints

********************************************************************************************
"""

from __future__ import annotations
import flask
from flask_cors import CORS
from . import routes
from tickle.common import url_converters
from tickle.common.config import configs
import flaskforward

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
    flask_app.register_blueprint(routes.bp_views, url_prefix='/')
    flask_app.register_blueprint(routes.bp_api, url_prefix='/api')


def _additionalConfig(flask_app: flask.Flask):
    flask_app.json_encoder = configs.Production.JSON_ENCODER
    
    flaskforward.globals.url = configs.Production.URL_API
    
    flaskforward.globals.headers = {
        configs.Production.SECURITY_HEADER_KEY: configs.Production.SECURITY_HEADER_VALUE,
    }


# Main logic
app = flask.Flask(__name__)
_setupCustomConverters(app)
_registerBlueprints(app)
_additionalConfig(app)
CORS(app)

