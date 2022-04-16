"""
********************************************************************************************

Watches repository

********************************************************************************************
"""

from __future__ import annotations
import requests

from tickle.common.config import configs


API_URL_PREFIX = 'https://api.tiingo.com'
API_URL_IEX = f'{API_URL_PREFIX}/iex'


def getTickerPrices(tickers: list[str]) -> list[dict]:


    prices_list = _getTickerPriceList(tickers)

    # serialize them into models and turn it into a dictionary


    return prices_list

    

def _getTickerPriceList(tickers: list[str]) -> list[dict]:
    tickers_str = _createTickerSymbolQueryString(tickers)
    parms = dict(tickers=tickers_str, token=configs.Dev.TICKER_API_TOKEN)

    try:
        response = _makeApiRequest(API_URL_IEX, parms)
        prices_list = response.json()
    except:
        prices_list = []

    return prices_list

    
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



def _makeApiRequest(url, query_parms) -> requests.Response:
    return requests.get(
        url = url,
        params=query_parms,
    )
