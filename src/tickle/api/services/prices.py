"""
********************************************************************************************

Prices services

********************************************************************************************
"""

from __future__ import annotations
from functools import wraps
import flask
from tickle.common import responses
from tickle import stockslib
from tickle.common.domain.views.stockslib import StocksApiPriceResponse


class ErrorMessages:
    MISSING_TAG_URL_ARG = 'Missing the required "tag" url parameter'


#------------------------------------------------------
# Decorator for isTagArgProvided
#------------------------------------------------------
def verifyRequiredUrlParm(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # if user is not logged in, redirect to login page
        if not isTagArgProvided():
            return responses.badRequest(ErrorMessages.MISSING_TAG_URL_ARG)

        return f(*args, **kwargs)

    return wrap


#------------------------------------------------------
# Checks that a 'tag' request url argument is provided by the client
# 
# Returns a bool:
#   true: it was provided
#   false: missing
#------------------------------------------------------
def isTagArgProvided() -> bool:
    tag = flask.request.args.get('tag') or None

    if not tag:
        return False
    else:
        return True

#------------------------------------------------------
# Get the price of the specified tag
#------------------------------------------------------
def getPrice(tag) -> StocksApiPriceResponse | None:
    price_map = stockslib.getPrices([tag])
    price = price_map.get(tag) or None
    return price
