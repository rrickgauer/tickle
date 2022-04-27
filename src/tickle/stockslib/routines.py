"""
********************************************************************************************

Routines for the investpy library

********************************************************************************************
"""


from __future__ import annotations
import investpy
from investpy.utils.search_obj import SearchObj
from tickle.common import serializers
from tickle.common.domain.views.stockslib import StocksApiSearchResponse
from tickle.common.domain.views.stockslib import StocksApiPriceResponse

INVESTPY_PRODUCTS = [
    # "indices",
    "stocks",
    "etfs",
    # "funds",
    # "commodities",
    # "currencies",
    "cryptos",
    # "bonds",
    # "certificates",
    # "fxfutures",
]

MAX_SEARCH_RESULTS = 20

def search(query):
    api_results = _getSearchResultsFromApi(query)
    return api_results


#------------------------------------------------------
# Fetch the search results from the api
#------------------------------------------------------
def _getSearchResultsFromApi(query) -> list[StocksApiSearchResponse]:
    try:
        api_results = _runApiQuoteSearch(query)
    except:
        api_results = []
    
    results = []
    
    for search_result in api_results:
        results.append(_serlializeSearchObj(search_result))

    return results

#------------------------------------------------------
# Use the stocks api to run a search
#------------------------------------------------------
def _runApiQuoteSearch(query) -> list[SearchObj]:
    search_results = investpy.search_quotes(
        text      = query,
        n_results = MAX_SEARCH_RESULTS,
        products  = INVESTPY_PRODUCTS,
    ) 

    return search_results

#------------------------------------------------------
# Serialize the specified search_obj into a SearchResponse view
#------------------------------------------------------
def _serlializeSearchObj(search_obj: SearchObj) -> StocksApiSearchResponse:
    serializer = serializers.StocksLibSearchResponseSerializer(search_obj.__dict__)
    result = serializer.serialize()
    return result

#------------------------------------------------------
# Get the price information for the specified tag
#------------------------------------------------------
def getPriceData(tag) -> StocksApiPriceResponse:
    search_obj     = _getEmptySearchObj()
    search_obj.tag = tag
    api_response   = search_obj.retrieve_information()
    price_view     = _toStocksApiPriceResponse(api_response)

    return price_view

#------------------------------------------------------
# Get an empty stocks api SearchObj
#------------------------------------------------------
def _getEmptySearchObj():
    search_obj = SearchObj(
        id_       = None,
        name      = None,
        symbol    = None,
        country   = None,
        tag       = None,
        pair_type = None,
        exchange  = None,
    )

    return search_obj

#------------------------------------------------------
# Serialize the given search object dictionary into a StocksApiPriceResponse view
#------------------------------------------------------
def _toStocksApiPriceResponse(search_obj_info: dict) -> StocksApiPriceResponse:
    serializer = serializers.StocksApiPriceResponseSerializer(search_obj_info)
    return serializer.serialize()
