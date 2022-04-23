"""
********************************************************************************************

Url Prefix: /api

********************************************************************************************
"""

from __future__ import annotations
import flask
import flaskforward

# module blueprint
bp_api = flask.Blueprint('api', __name__)


#------------------------------------------------------
#
#------------------------------------------------------
@bp_api.get('search/tickers/crypto')
def searchCryptoTickers():
    response = flaskforward.routines.sendExternalRequest(flask.request, '/search/tickers/crypto')
    return flaskforward.routines.toFlaskResponse(response)