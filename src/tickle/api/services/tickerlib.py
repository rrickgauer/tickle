"""
********************************************************************************************

Watches repository

********************************************************************************************
"""

from __future__ import annotations
import requests
from tickle.common.config import configs
from tickle.common import serializers
from tickle.common.views.tiingo import TickerResponse
from tickle.common.utilities import getConfig

#------------------------------------------------------
# Get a dictionary of TickerResponses for the specified ticker symbols
# The keys are the ticker symbols
#------------------------------------------------------
def getTickerPrices(tickers: list[str]) -> dict[str, TickerResponse]:
    prices_list = _getTickerPricesList(tickers)
    return _toDict(prices_list)

#------------------------------------------------------
# Get a list of TickerResponses for the specified ticker symbols
#------------------------------------------------------
def _getTickerPricesList(tickers: list[str]) -> list[TickerResponse]:
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
    tickers_str = _createTickerSymbolQueryString(tickers)
    
    parms = dict(
        tickers = tickers_str,
    )

    config = getConfig()

    try:
        response = _makeApiRequest(config.STOCK_PRICE_API_URL_IEX, parms)
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
# Make the api request to get the stock prices
#------------------------------------------------------
def _makeApiRequest(url: str, query_parms: dict=None) -> requests.Response:
    if not query_parms:
        query_parms = {}

    query_parms.setdefault('token', configs.Production.STOCK_PRICE_API_TOKEN)
    
    return requests.get(
        url = url,
        params=query_parms,
    )

#------------------------------------------------------
# Serialze the given dictionary into a TickerResponse object
#------------------------------------------------------
def _serializeTickerResponseDict(ticker_price_dict: dict) -> TickerResponse:
    serializer = serializers.TickerResponseSerializer(ticker_price_dict)
    model = serializer.serialize()
    return model

#------------------------------------------------------
# Transform the given TickerResponse list into a dictionary with each key being the ticker
#------------------------------------------------------
def _toDict(ticker_prices: list[TickerResponse]) -> dict[str, TickerResponse]:
    result = {}

    for ticker_price in ticker_prices:
        result.setdefault(ticker_price.ticker, ticker_price)
    
    return result
