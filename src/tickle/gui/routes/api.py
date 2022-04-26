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

    # url = 'http://api.tickle.ryanrickgauer.com:5010/v1/search/tickers/stocks'
    # parms = flask.request.args.to_dict()

    # response = requests.get(url, params=parms)
    
    # lineBreak(5)
    # print(response.text)
    # lineBreak(5)

    # if not response.ok:
    #     return response.text
    
    # return flask.jsonify(response.json().get('data'))

    # return 'got it'

    url = f'{getConfig().URL_API}/search/tickers/stocks'

    lineBreak(5)
    print(url)
    lineBreak(5)

    response = flaskforward.routines.sendRequest(flaskforward.structs.SingleRequest(
        method='get',
        url    = url,
        params = flask.request.args.to_dict(),
    ))

    return flaskforward.routines.toFlaskResponse(response)


    api_response = flaskforward.routines.sendExternalRequest(flask.request, '/search/tickers/stocks')
    return flaskforward.routines.toFlaskResponse(api_response)


#------------------------------------------------------
# Create a new watch
#------------------------------------------------------
@bp_api.post('watches')
def createWatch():
    api_response = flaskforward.routines.sendExternalRequest(flask.request, '/watches')
    return flaskforward.routines.toFlaskResponse(api_response)