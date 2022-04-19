"""
********************************************************************************************

Url Prefix: /internal

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.api import services
from tickle.common import responses

# module blueprint
bp_internal = flask.Blueprint('internal', __name__)

#------------------------------------------------------
# Audit endpoint
# Internal use only
#------------------------------------------------------
@bp_internal.route('audit')
def testCheck():
    open_watches = services.audit.getOpenWatches()
    ticker_symbols = list(open_watches.keys())
    prices = services.tickerlib.getTickerPrices(ticker_symbols)

    watches_to_confirm = services.audit.runPriceChecks(open_watches, prices)

    return responses.get(watches_to_confirm)

    return responses.get(dict(
        symbols = ticker_symbols,
        watches = open_watches,
        prices = prices,
        confirmation_candiates = watches_to_confirm,
    ))

    return flask.jsonify(prices)