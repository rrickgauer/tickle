"""
********************************************************************************************

Url Prefix: /api

********************************************************************************************
"""

from __future__ import annotations
import flask
import flaskforward
import requests
from tickle.common.utilities import lineBreak, getConfig

# module blueprint
bp_api = flask.Blueprint('api', __name__)

#------------------------------------------------------
# search for crypto tickers
#------------------------------------------------------
@bp_api.get('search/tickers/crypto')
def searchCryptoTickers():
    return _sendRequest('search/tickers/crypto')

    # url = 'http://api.tickle.ryanrickgauer.com:5010/v1/watches'

    # response = requests.get(url)

    # # return 'sup'

    # print(response.ok)


    api_response = flaskforward.routines.sendExternalRequest(flask.request, '/search/tickers/crypto')
    return flaskforward.routines.toFlaskResponse(api_response)

#------------------------------------------------------
# search for stock tickers
#------------------------------------------------------
@bp_api.get('search/tickers/stocks')
def searchStockTickers():
    return _sendRequest('search/tickers/stocks')
    # url = f'{getConfig().URL_API}/search/tickers/stocks'

    # response = flaskforward.routines.sendRequest(flaskforward.structs.SingleRequest(
    #     method='get',
    #     url    = url,
    #     params = flask.request.args.to_dict(),
    # ))

    # return flaskforward.routines.toFlaskResponse(response)


    # api_response = flaskforward.routines.sendExternalRequest(flask.request, '/search/tickers/stocks')
    # return flaskforward.routines.toFlaskResponse(api_response)


#------------------------------------------------------
# Create a new watch
#------------------------------------------------------
@bp_api.post('watches')
def createWatch():
    return _sendRequest('watches')
    api_response = flaskforward.routines.sendExternalRequest(flask.request, '/watches')
    return flaskforward.routines.toFlaskResponse(api_response)


def _sendRequest(endpoint):
    url = f'{getConfig().URL_API}/{endpoint}'

    single_request = flaskforward.structs.SingleRequest(
        method = flask.request.method,
        url    = url,
        params = flask.request.args.to_dict(),
        data   = flask.request.form.to_dict(),
    )

    api_response = flaskforward.routines.sendRequest(single_request)
    return flaskforward.routines.toFlaskResponse(api_response)
