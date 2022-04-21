"""
********************************************************************************************

Tiingo api services.

This is a wrapper for calling the stocks api: api.tiingo.com.

********************************************************************************************
"""

from __future__ import annotations
from tickle.common import serializers
from tickle.common.domain.views.tiingo import StockTickerPrice
from tickle.api.services.tickerlib.constants import StockPriceApiUrls
from tickle.api.services.tickerlib.utilities import makeApiRequest, createSymbolQueryString


#------------------------------------------------------
# Get a dictionary of TickerResponses for the specified ticker symbols
# The keys are the ticker symbols
#------------------------------------------------------
def getStockPrices(tickers: list[str]) -> dict[str, StockTickerPrice]:
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
        tickers = createSymbolQueryString(tickers),
    )

    try:
        response = makeApiRequest(StockPriceApiUrls.IEX, parms)
        prices_list = response.json()
    except:
        prices_list = []

    return prices_list





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








