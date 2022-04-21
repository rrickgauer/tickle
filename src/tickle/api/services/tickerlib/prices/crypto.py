"""
********************************************************************************************

This module is responsible for fetching the crypto prices from the stocks api: api.tiingo.com.

********************************************************************************************
"""

from __future__ import annotations
from tickle.api.services.tickerlib.constants import StockPriceApiUrls
from tickle.api.services.tickerlib.utilities import createSymbolQueryString, makeApiRequest
from tickle.common.domain.enums.watches import TickerTypes
from tickle.common.domain.models import TickerPrice
from tickle.common.domain.models import TickerPriceMap
from tickle.common.domain.views.tiingo import CryptoTickerPrice
from tickle.common import serializers


#------------------------------------------------------
# Get the prices for the given list of crypto tickers
#------------------------------------------------------
def getCryptoPrices(tickers: list[str]) -> TickerPriceMap:
    api_response_data = _getPricesFromApi(tickers)
    prices_list = _serializeApiResponseData(api_response_data)
    prices_map = _toTickerPriceMap(prices_list)
    return prices_map

#------------------------------------------------------
# Make an http request to the stocks api to fetch the prices of the specified crypto coins
#------------------------------------------------------
def _getPricesFromApi(tickers: list[str]) -> list[dict]:
    request_parms = dict(
        tickers = createSymbolQueryString(tickers)
    )

    api_response = makeApiRequest(StockPriceApiUrls.CRYPTO_PRICES, request_parms)

    if not api_response.ok:
        raise Exception(str(api_response.text))

    try:
        return api_response.json()
    except:
        return []

#------------------------------------------------------
# serialize the given list of dictionaries into a list of CryptoTickerPrice
#------------------------------------------------------
def _serializeApiResponseData(api_data_records: list[dict]) -> list[CryptoTickerPrice]:
    crypto_ticker_prices = []

    for record in api_data_records:
        serializer = serializers.CryptoTickerPriceSerializer(record)
        result = serializer.serialize()
        crypto_ticker_prices.append(result)
    
    return crypto_ticker_prices

#------------------------------------------------------
# Convert the specified CryptoTickerPrice object into a TickerPriceMap
#------------------------------------------------------
def _toTickerPriceMap(crypto_ticker_prices: list[CryptoTickerPrice]) -> TickerPriceMap:
    result = {}

    for crypto_price in crypto_ticker_prices:
        ticker_price = _toTickerPrice(crypto_price)
        result.setdefault(ticker_price.ticker, ticker_price)

    return result

#------------------------------------------------------
# Convert the speicified CryptoTickerPrice into a TickerPrice object
#------------------------------------------------------
def _toTickerPrice(crypto_price: CryptoTickerPrice) -> TickerPrice:
    ticker_price = TickerPrice(
        ticker      = crypto_price.ticker,
        ticker_type = TickerTypes.CRYPTO,
        price       = crypto_price.topOfBookData.lastPrice or crypto_price.topOfBookData.askPrice,
    )

    return ticker_price


    

