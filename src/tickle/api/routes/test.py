"""
********************************************************************************************

Url Prefix: /test

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.common import responses
from tickle.api import security
from tickle import stockslib
from tickle.common.utilities import dumpJson
import investpy

from tickle.common.domain.enums.watches import PairTypes


# module blueprint
bp_test = flask.Blueprint('test', __name__)

#------------------------------------------------------
# Test endpoint
#------------------------------------------------------
@bp_test.route('')
# @security.localEndpoint
def test():
    security.isRequestLocal()
    return responses.get('test endpoint')



#------------------------------------------------------
# Test investpy
#------------------------------------------------------
@bp_test.route('investpy')
def testInvestpy():
    prices = stockslib.testprices.testSequential()
    return responses.get(prices)


#------------------------------------------------------
# Test investpy
#------------------------------------------------------
@bp_test.route('investpy/5')
def testInvestpy5():
    tags = stockslib.test_tags.TEST_TAGS
    prices = stockslib.routines.getPrices(tags)
    return responses.get(prices)


#------------------------------------------------------
# Test investpy
#------------------------------------------------------
@bp_test.route('investpy/<test_converter>')
def testConverter(test_converter):


    output = dict(
        # crypto_search = investpy.crypto.search_cryptos('symbol', 'DOGE').to_dict('records'),
        crypto_dict = investpy.crypto.get_cryptos_dict()[:20],
        # stocks_list = investpy.stocks.get_stocks_list()[:20],
        stocks_dict = investpy.stocks.get_stocks_dict()[:20],
    )


    return flask.jsonify(output)
    
    dumpJson(flask.request.args.to_dict())
    return str(test_converter)