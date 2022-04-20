"""
********************************************************************************************

Url Prefix: /internal

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.api import services
from tickle.common import responses
from tickle.api.services.audit.auditor import StocksAuditor

# module blueprint
bp_internal = flask.Blueprint('internal', __name__)

#------------------------------------------------------
# Audit endpoint
# Internal use only
# /internal/audit
#------------------------------------------------------
@bp_internal.route('audit')
def performAudit():
    open_watches_map = services.watches.getOpenWatches()
    auditor = StocksAuditor(open_watches_map.stocks)
    watches_to_close = auditor.runPriceChecks()
    
    return responses.get(watches_to_close)




    # ticker_symbols = list(open_watches_map.keys())
    # prices = services.tickerlib.getTickerPrices(ticker_symbols)


    # watches_to_confirm = services.audit.runPriceChecks(open_watches_map, prices)

    # return responses.get(watches_to_confirm)

    # return responses.get(dict(
    #     symbols = ticker_symbols,
    #     watches = open_watches_map,
    #     prices = prices,
    #     confirmation_candiates = watches_to_confirm,
    # ))

    # return flask.jsonify(prices)


#------------------------------------------------------
# Fetch and save the crypto tickers from the api
# /internal/fetch-crypto-tickers
#------------------------------------------------------
@bp_internal.route('fetch-crypto-tickers')
def fetchCryptoTickers():
    # result = services.tickerlib.saveAllCryptoTickerSymbols()
    # return responses.created(result)

    return 'fetch'


