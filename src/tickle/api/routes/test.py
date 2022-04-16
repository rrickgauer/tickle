"""
********************************************************************************************

Url Prefix: /test

********************************************************************************************
"""

from __future__ import annotations
import flask

from tickle.api import services

from tickle.common import responses


# module blueprint
bp_test = flask.Blueprint('test', __name__)

#------------------------------------------------------
# Test endpoint
#------------------------------------------------------
@bp_test.route('')
def test():

    result = services.email.sendEmail()

    return 'test endpoint'

        
#------------------------------------------------------
# Test endpoint
#------------------------------------------------------
@bp_test.route('check')
def testCheck():

    data = services.inspector.getOpenWatches()
    ticker_symbols = list(data.keys())
    prices = services.tickerlib.getTickerPrices(ticker_symbols)

    return responses.get(dict(
        symbols = ticker_symbols,
        watches = data,
        prices = prices
    ))

    return flask.jsonify(prices)


