"""
********************************************************************************************

Url Prefix: /api

********************************************************************************************
"""

from __future__ import annotations
import flask
import flaskforward
from tickle.common.utilities import getConfig

# module blueprint
bp_api = flask.Blueprint('api', __name__)

#------------------------------------------------------
# search for crypto tickers
#------------------------------------------------------
@bp_api.get('search/tickers/crypto')
def searchCryptoTickers():
    return _sendRequest('search/tickers/crypto')

#------------------------------------------------------
# search for stock tickers
#------------------------------------------------------
@bp_api.get('search/tickers/stocks')
def searchStockTickers():
    return _sendRequest('search/tickers/stocks')

#------------------------------------------------------
# Create a new watch
#------------------------------------------------------
@bp_api.post('watches')
def createWatch():
    return _sendRequest('watches')


#------------------------------------------------------
# Send external request
#------------------------------------------------------
def _sendRequest(endpoint):
    config = getConfig()
    
    url = f'{config.URL_API}/{endpoint}'

    headers = {
        config.SECURITY_HEADER_KEY: config.SECURITY_HEADER_VALUE,
    }

    single_request = flaskforward.structs.SingleRequest(
        method  = flask.request.method,
        url     = url,
        params  = flask.request.args.to_dict(),
        data    = flask.request.form.to_dict(),
        headers = headers,
    )

    api_response = flaskforward.routines.sendRequest(single_request)
    return flaskforward.routines.toFlaskResponse(api_response)
