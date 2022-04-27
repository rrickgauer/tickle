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


# module blueprint
bp_test = flask.Blueprint('test', __name__)

#------------------------------------------------------
# Test endpoint
#------------------------------------------------------
@bp_test.route('')
@security.localEndpoint
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