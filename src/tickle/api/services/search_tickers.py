"""
********************************************************************************************

Ticker search services

********************************************************************************************
"""

from __future__ import annotations
from functools import wraps
import flask
from tickle.common import responses
from tickle.common import serializers
from tickle.common.responses.errors import SearchTickersMissingQArgError
from tickle.common.views.tiingo import CryptoSymbolApiResponse
from tickle.common.views.tiingo import StockSearchApiResponse
from . import tickerlib
import tickle.api.repository.crypto_tickers as crypto_repo

#------------------------------------------------------
# Search the stocks api for the given stock symbol query
#------------------------------------------------------
def searchStocks(query: str) -> list[StockSearchApiResponse]:
    # make a request to the stock api
    api_response = _sendStockSearchRequest(query)

    # transform the api response data into a list of dictionaries
    try:
        api_search_results = api_response.json()
    except Exception as ex:
        print(ex)
        api_search_results = []

    views = _serializeStockSearchApiResponseObjects(api_search_results)
    return views
    
#------------------------------------------------------
# Send a search request ot the stocks api
#------------------------------------------------------
def _sendStockSearchRequest(query: str):
    api_request_url_parms = dict(query=query)
    api_response = tickerlib.makeApiRequest(tickerlib.StockPriceApiUrls.SEARCH_SYMBOLS, api_request_url_parms)
    
    if not api_response.ok:
        print(api_response.text)
        flask.abort(500)

    return api_response


#------------------------------------------------------
# Serialize the given list of dictionaries into StockSearchApiResponse views
#------------------------------------------------------
def _serializeStockSearchApiResponseObjects(api_search_results: list[dict]) -> list[StockSearchApiResponse]:
    views = []

    for api_response_dict in api_search_results:
        serializer = serializers.StockSearchApiResponseSerializer(api_response_dict)
        serialized_view = serializer.serialize()
        views.append(serialized_view)

    return views

#------------------------------------------------------
# Search the database for any crypto tickers that match the specified query
#------------------------------------------------------
def searchCrypto(query: str) -> list[CryptoSymbolApiResponse]:
    db_result = _getCryptoRepoSearchResults(query)

    # serialize them into views
    views = []
    for d in db_result:
        view = serializers.CryptoSymbolApiResponseSerializer(d).serialize()
        views.append(view)

    return views

#------------------------------------------------------
# Get the search results from the database
#------------------------------------------------------
def _getCryptoRepoSearchResults(query) -> list[dict]:
    db_result = crypto_repo.search(query)

    if not db_result.successful:
        raise db_result.error

    data = db_result.data[0] or []

    return data


#------------------------------------------------------
# Decorator for isQueryUrlRequestParmPresent
#------------------------------------------------------
def verifyRequiredUrlParm(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # if user is not logged in, redirect to login page
        if not isQueryUrlRequestParmPresent():
            return responses.badRequest(SearchTickersMissingQArgError)

        return f(*args, **kwargs)

    return wrap

#------------------------------------------------------
# Checks if the current request provided the required 'q' url parm 
#------------------------------------------------------
def isQueryUrlRequestParmPresent() -> bool:
    query_val = flask.request.args.get('q') or None

    if query_val:
        return True
    else:
        return False





