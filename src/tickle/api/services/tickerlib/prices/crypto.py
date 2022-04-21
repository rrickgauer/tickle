"""
********************************************************************************************

This module is responsible for fetching the crypto prices from the stocks api: api.tiingo.com.

********************************************************************************************
"""

from __future__ import annotations
from tickle.api.services.tickerlib.constants import StockPriceApiUrls
from tickle.api.services.tickerlib.utilities import createSymbolQueryString, makeApiRequest
from tickle.common.domain.models.ticker_price import TickerPrice
from tickle.common.domain.views.tiingo import CryptoTickerPrice
from tickle.common.utilities import dumpJson
from tickle.common import serializers


def getCryptoPrices(tickers: list[str]) -> dict[str, TickerPrice]:
    api_response = _getPricesFromApi(tickers)
    prices_list = _serializeApiResponse(api_response)



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


# serialize the given list of dictionaries into a list of CryptoTickerPrice
def _serializeApiResponse(api_data_records: list[dict]) -> list[CryptoTickerPrice]:
    crypto_ticker_prices = []

    for record in api_data_records:
        serializer = serializers.CryptoTickerPriceSerializer(record)
        result = serializer.serialize()

        crypto_ticker_prices.append(result)
    
    return crypto_ticker_prices







    

