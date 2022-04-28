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
from tickle import stockslib

# module blueprint
bp_search_tickers = flask.Blueprint('search_tickers', __name__)

#------------------------------------------------------
# New search
#
# /search/tickers?q={query}
#------------------------------------------------------
@bp_search_tickers.get('')
@security.localEndpoint
@services.search_tickers.verifyRequiredUrlParm
def searchTickers():
    query = flask.request.args.get('q') or None
    search_results = stockslib.search(query)
    return responses.get(search_results)