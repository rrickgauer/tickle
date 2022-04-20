"""
********************************************************************************************

Url Prefix: /search/tickers

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.api import services
from tickle.common import responses

# module blueprint
bp_search_tickers = flask.Blueprint('search_tickers', __name__)

#------------------------------------------------------
# Search for stock tickers
#------------------------------------------------------
@bp_search_tickers.get('stocks')
@services.search_tickers.verifyRequiredUrlParm
def searchStocks():
    query = flask.request.args.get('q')
    search_result = services.search_tickers.searchStocks(query)
    return responses.get(search_result)

#------------------------------------------------------
# Search for crypto tickers
#------------------------------------------------------
@bp_search_tickers.get('crypto')
@services.search_tickers.verifyRequiredUrlParm
def searchCrypto():
    query = flask.request.args.get('q')
    results = services.search_tickers.searchCrypto(query)
    return responses.get(results)