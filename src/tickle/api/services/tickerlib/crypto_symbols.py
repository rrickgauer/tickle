
"""
********************************************************************************************

Get all the crypto symbols from the stocks api.

********************************************************************************************
"""

from __future__ import annotations
from tickle.common.domain.views.tiingo import CryptoSymbolApiResponse
from tickle.common import serializers
from tickle.api.services.tickerlib.utilities import makeApiRequest
from tickle.api.services.tickerlib.constants import StockPriceApiUrls

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
