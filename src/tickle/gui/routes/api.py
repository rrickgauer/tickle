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
# search for crypto tickers
#------------------------------------------------------
@bp_api.get('search/tickers/crypto')
def searchCryptoTickers():
    api_response = flaskforward.routines.sendExternalRequest(flask.request, '/search/tickers/crypto')
    return flaskforward.routines.toFlaskResponse(api_response)

#------------------------------------------------------
# search for stock tickers
#------------------------------------------------------
@bp_api.get('search/tickers/stocks')
def searchStockTickers():
    api_response = flaskforward.routines.sendExternalRequest(flask.request, '/search/tickers/stocks')
    return flaskforward.routines.toFlaskResponse(api_response)


#------------------------------------------------------
# Create a new watch
#------------------------------------------------------
@bp_api.post('watches')
def createWatch():
    api_response = flaskforward.routines.sendExternalRequest(flask.request, '/watches')
    return flaskforward.routines.toFlaskResponse(api_response)