"""
********************************************************************************************

Url Prefix: /internal

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.api import services
from tickle.common import responses
from tickle.api.services.audit.auditor import CryptoAuditor, StocksAuditor
from tickle.api.services.tickerlib import prices

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

    # perform an audit for the stock watches
    stocks_auditor = StocksAuditor(open_watches_map.stocks)
    crypto_auditor = CryptoAuditor(open_watches_map.crypto)

    watches_to_close = [
        *stocks_auditor.runPriceChecks(),
        *crypto_auditor.runPriceChecks(),
    ]

    
    return responses.get(watches_to_close)



#------------------------------------------------------
# Fetch and save the crypto tickers from the api
# /internal/fetch-crypto-tickers
#------------------------------------------------------
@bp_internal.route('fetch-crypto-tickers')
def fetchCryptoTickers():
    # result = services.tickerlib.saveAllCryptoTickerSymbols()
    # return responses.created(result)

    return 'fetch'


