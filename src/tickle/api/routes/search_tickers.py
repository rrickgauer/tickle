"""
********************************************************************************************

Url Prefix: /search/tickers

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.api import services
from tickle.common import responses
from tickle.api import security

# module blueprint
bp_search_tickers = flask.Blueprint('search_tickers', __name__)

#------------------------------------------------------
# Search for stock tickers
#
# /search/tickers/stocks?q={query}
#------------------------------------------------------
@bp_search_tickers.get('stocks')
@security.localEndpoint
@services.search_tickers.verifyRequiredUrlParm
def searchStocks():
    query = flask.request.args.get('q')
    search_result = services.search_tickers.searchStocks(query)
    return responses.get(search_result)

#------------------------------------------------------
# Search for crypto tickers
#
# /search/tickers/crypto?q={query}
#------------------------------------------------------
@bp_search_tickers.get('crypto')
@security.localEndpoint
@services.search_tickers.verifyRequiredUrlParm
def searchCrypto():
    query = flask.request.args.get('q')
    results = services.search_tickers.searchCrypto(query)
    return responses.get(results)