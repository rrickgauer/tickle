"""
********************************************************************************************

Url Prefix: /test

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.common import responses
from tickle.api import security


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


