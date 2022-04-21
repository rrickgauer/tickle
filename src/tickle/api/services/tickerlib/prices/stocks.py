"""
********************************************************************************************

This module is responsible for fetching the stock prices from the stocks api: api.tiingo.com.

********************************************************************************************
"""

from __future__ import annotations
from tickle.common import serializers
from tickle.common.domain.enums.watches import TickerTypes
from tickle.common.domain.views.tiingo import StockTickerPrice
from tickle.api.services.tickerlib.constants import StockPriceApiUrls
from tickle.api.services.tickerlib.utilities import makeApiRequest, createSymbolQueryString
from tickle.common.domain.models.ticker_price import TickerPrice


#------------------------------------------------------
# Get a dictionary of TickerResponses for the specified ticker symbols
# The keys are the ticker symbols
#------------------------------------------------------
def getStockPrices(tickers: list[str]) -> dict[str, TickerPrice]:
    prices_list = _getStockPricesList(tickers)
    price_map = _toTickerPriceMap(prices_list)
    return price_map

#------------------------------------------------------
# Get a list of TickerResponses for the specified ticker symbols
#------------------------------------------------------
def _getStockPricesList(tickers: list[str]) -> list[StockTickerPrice]:
    # call the api to fetch the raw data price dictionaries
    api_response = _getStockPricesListFromApi(tickers)

    # serialize the api response dictionaries into view models
    price_models = _toStockTickerPriceList(api_response)
    
    return price_models


#------------------------------------------------------
# Get the api's ticker price information
#
# Args:
#   tickers: the list of tickers to send to the api
#
# Returns the api response
#------------------------------------------------------
def _getStockPricesListFromApi(tickers: list[str]) -> list[dict]:    
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
# Serialize the list of dictionaries into view models
#------------------------------------------------------
def _toStockTickerPriceList(records: list[dict]) -> list[StockTickerPrice]:
    price_models = []

    for api_response_dict in records:
        model = _toStockTickerPrice(api_response_dict)
        price_models.append(model)

    return price_models


#------------------------------------------------------
# Serialze the given dictionary into a TickerResponse object
#------------------------------------------------------
def _toStockTickerPrice(ticker_price_dict: dict) -> StockTickerPrice:
    serializer = serializers.TickerResponseSerializer(ticker_price_dict)
    model = serializer.serialize()
    return model

#------------------------------------------------------
# Transform the given TickerResponses into a dictionary of TickerPrice models
# Each key being the ticker
#------------------------------------------------------
def _toTickerPriceMap(stock_ticker_prices: list[StockTickerPrice]) -> dict[str, TickerPrice]:
    result = {}

    for stock_ticker_price in stock_ticker_prices:
        ticker_price = _toTickerPrice(stock_ticker_price)
        result.setdefault(stock_ticker_price.ticker, ticker_price)
    
    return result

#------------------------------------------------------
# Transform the specified StockTickerPrice view into a TickerPrice model
#------------------------------------------------------
def _toTickerPrice(stock_ticker_price: StockTickerPrice) -> TickerPrice:
    ticker_price = TickerPrice(
        ticker      = stock_ticker_price.ticker,
        ticker_type = TickerTypes.STOCKS,
        price       = stock_ticker_price.last,
    )

    return ticker_price





