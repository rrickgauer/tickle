"""
********************************************************************************************

Routines for the investpy library

********************************************************************************************
"""


from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import investpy
from investpy.utils.search_obj import SearchObj
from tickle.common import serializers
from tickle.common.domain.views.stockslib import StocksApiSearchResponse, StocksApiPriceResponse
from .constants import INVESTPY_PRODUCTS, MAX_SEARCH_RESULTS, PRICE_THREAD_CHUNK_SIZE


# Search the stocks api for the financial product
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
# Get the prices for the specified tags
#------------------------------------------------------
def getPrices(tags: list[str]) -> list[StocksApiPriceResponse]:
    prices = _getPricesMultiThreaded(tags)
    return prices

#------------------------------------------------------
# Using threads, fetch the prices of the specified list of tags
#------------------------------------------------------
def _getPricesMultiThreaded(tags: list) -> list[StocksApiPriceResponse]:
    chunk_size = PRICE_THREAD_CHUNK_SIZE
    num_chunks = len(tags)
    executor = ThreadPoolExecutor(max_workers=num_chunks)
    prices = []
    threads = []

    for i in range(num_chunks):
        # place a subset of tags into a thread
        starting_index = i * chunk_size
        last_index = (i + 1) * chunk_size
        chunk = tags[starting_index:last_index]

        if len(chunk) == 0:
            break
        
        # add the thread to the pool
        threads.append(executor.submit(_setTagPrices, chunk, prices))
    
    # execute all the threads
    for _ in concurrent.futures.as_completed(threads):
        pass

    return prices

#------------------------------------------------------
# Append the prices for the specified tags to the given list of prices
#------------------------------------------------------
def _setTagPrices(tags: list[str], prices: list) -> list[StocksApiPriceResponse]:
    for tag in tags:
        price = _getTagPrice(tag)
        prices.append(price)

#------------------------------------------------------
# Get the price information for the specified tag
#------------------------------------------------------
def _getTagPrice(tag) -> StocksApiPriceResponse:
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
