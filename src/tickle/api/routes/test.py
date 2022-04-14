"""
********************************************************************************************

Url Prefix: /test

********************************************************************************************
"""

from __future__ import annotations
import flask

from tickle.api import services


# module blueprint
bp_test = flask.Blueprint('test', __name__)

#------------------------------------------------------
# Test endpoint
#------------------------------------------------------
@bp_test.route('')
def test():

    result = services.email.sendEmail()

    return 'test endpoint'

        



