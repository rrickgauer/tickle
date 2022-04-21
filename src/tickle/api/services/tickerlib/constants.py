"""
********************************************************************************************

Tiingo api constants/enums

********************************************************************************************
"""

from __future__ import annotations


class StockPriceApiUrls:
    BASE               = 'https://api.tiingo.com'
    IEX                = f'{BASE}/iex'
    SEARCH_SYMBOLS     = f'{BASE}/tiingo/utilities/search'
    CRYPTO_ALL_TICKERS = f'{BASE}/tiingo/crypto'