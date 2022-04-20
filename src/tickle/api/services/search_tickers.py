"""
********************************************************************************************

Ticker search services

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.common import serializers
from tickle.common.views.tiingo import StockSearchApiResponse
from . import tickerlib

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







