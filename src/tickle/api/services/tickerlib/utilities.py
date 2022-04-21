


from __future__ import annotations
import requests
from tickle.common.utilities import getConfig


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


#------------------------------------------------------
# create the tickers request url parm string:
#
# Example: 
#   input: 'aapl', 'spy', 'amzn' 
#   output: aapl,spy,amzn
#------------------------------------------------------
def createSymbolQueryString(tickers: list[str]) -> str:
    tickers_str = ''
    is_first = True

    for ticker in tickers:
        if is_first:
            is_first = False
            tickers_str = f'{ticker}'
        else:
            tickers_str += f',{ticker}'

    return tickers_str