"""
********************************************************************************************

Url Prefix: /test

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.common import responses
from tickle.common.email import messenger

# module blueprint
bp_test = flask.Blueprint('test', __name__)

#------------------------------------------------------
# Test endpoint
#------------------------------------------------------
@bp_test.route('')
def test():

    # messenger.sendEmail()

    return responses.get('test endpoint')


