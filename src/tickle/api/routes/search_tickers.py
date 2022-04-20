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
@bp_search_tickers.get('stocks/<string:query>')
def searchStocks(query: str):
    search_result = services.search_tickers.searchStocks(query)
    return responses.get(search_result)

#------------------------------------------------------
# Search for crypto tickers
#------------------------------------------------------
@bp_search_tickers.get('crypto/<string:query>')
def searchCrypto(query: str):
    return 'search crypto'