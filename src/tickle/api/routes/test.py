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

    open_watches = services.inspector.getOpenWatches()
    ticker_symbols = list(open_watches.keys())
    prices = services.tickerlib.getTickerPrices(ticker_symbols)

    watches_to_confirm = services.inspector.runPriceChecks(open_watches, prices)

    return responses.get(watches_to_confirm)

    return responses.get(dict(
        symbols = ticker_symbols,
        watches = open_watches,
        prices = prices,
        confirmation_candiates = watches_to_confirm,
    ))

    return flask.jsonify(prices)


