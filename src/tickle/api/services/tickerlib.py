"""
********************************************************************************************

Tiingo api services.

This is a wrapper for calling the stocks api: api.tiingo.com.

********************************************************************************************
"""

from __future__ import annotations
import flask
import requests
from tickle.common import serializers
from tickle.common.domain.views.tiingo import CryptoSymbolApiResponse
from tickle.common.domain.views.tiingo import StockTickerPrice
from tickle.common.utilities import getConfig

class StockPriceApiUrls:
    BASE               = 'https://api.tiingo.com'
    IEX                = f'{BASE}/iex'
    SEARCH_SYMBOLS     = f'{BASE}/tiingo/utilities/search'
    CRYPTO_ALL_TICKERS = f'{BASE}/tiingo/crypto'

#------------------------------------------------------
# Get a dictionary of TickerResponses for the specified ticker symbols
# The keys are the ticker symbols
#------------------------------------------------------
def getTickerPrices(tickers: list[str]) -> dict[str, StockTickerPrice]:
    prices_list = _getTickerPricesList(tickers)
    return _toTickerMap(prices_list)

#------------------------------------------------------
# Get a list of TickerResponses for the specified ticker symbols
#------------------------------------------------------
def _getTickerPricesList(tickers: list[str]) -> list[StockTickerPrice]:
    # call the api to fetch the raw data prices
    prices_api_response = _getTickerPriceListFromApi(tickers)

    price_models = []
    
    # serialize the api response dictionaries into view models
    for api_response_dict in prices_api_response:
        model = _serializeTickerResponseDict(api_response_dict)
        price_models.append(model)

    return price_models


#------------------------------------------------------
# Get the api's ticker price information
#
# Args:
#   tickers: the list of tickers to send to the api
#
# Returns the api response
#------------------------------------------------------
def _getTickerPriceListFromApi(tickers: list[str]) -> list[dict]:    
    parms = dict(
        tickers = _createTickerSymbolQueryString(tickers),
    )

    try:
        response = makeApiRequest(StockPriceApiUrls.IEX, parms)
        prices_list = response.json()
    except:
        prices_list = []

    return prices_list

#------------------------------------------------------
# create the tickers request url parm string:
#
# Example: 
#   input: 'aapl', 'spy', 'amzn' 
#   output: aapl,spy,amzn
#------------------------------------------------------
def _createTickerSymbolQueryString(tickers: list[str]) -> str:
    tickers_str = ''
    is_first = True

    for ticker in tickers:
        if is_first:
            is_first = False
            tickers_str = f'{ticker}'
        else:
            tickers_str += f',{ticker}'

    return tickers_str



#------------------------------------------------------
# Serialze the given dictionary into a TickerResponse object
#------------------------------------------------------
def _serializeTickerResponseDict(ticker_price_dict: dict) -> StockTickerPrice:
    serializer = serializers.TickerResponseSerializer(ticker_price_dict)
    model = serializer.serialize()
    return model

#------------------------------------------------------
# Transform the given TickerResponse list into a dictionary with each key being the ticker
#------------------------------------------------------
def _toTickerMap(ticker_prices: list[StockTickerPrice]) -> dict[str, StockTickerPrice]:
    result = {}

    for ticker_price in ticker_prices:
        result.setdefault(ticker_price.ticker, ticker_price)
    
    return result





#------------------------------------------------------
# Get a list of CryptoSymbolApiResponse that are in the api
#------------------------------------------------------
def getAllCryptoTickerSymbols() -> list[CryptoSymbolApiResponse]:
    crypto_tickers = []

    for ticker_dict in _getAllCryptoTickersFromApi():            
        serializer = serializers.CryptoSymbolApiResponseSerializer(ticker_dict)
        crypto_tickers.append(serializer.serialize())

    return crypto_tickers

#------------------------------------------------------
# Get a list of all the crypto ticker symbols from the stock api
#------------------------------------------------------
def _getAllCryptoTickersFromApi() -> list[dict]:
    url = StockPriceApiUrls.CRYPTO_ALL_TICKERS

    api_response = makeApiRequest(url)

    if not api_response.ok:
        raise api_response.text

    try:
        return api_response.json()
    except:
        return []



#------------------------------------------------------
# Make an http request to the api
#
# Args:
#   url: the api endpoint to use
#   query_parms: the url search paramters to include in the request
#
# Returns: the api response
#------------------------------------------------------
def makeApiRequest(url: str, query_parms: dict=None) -> requests.Response:
    if not query_parms:
        query_parms = {}

    query_parms.setdefault('token', getConfig().STOCK_PRICE_API_TOKEN)
    
    return requests.get(
        url    = url,
        params = query_parms,
    )
