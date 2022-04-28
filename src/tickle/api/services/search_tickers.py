"""
********************************************************************************************

Ticker search services

********************************************************************************************
"""

from __future__ import annotations
from functools import wraps
import flask
from tickle.common import responses
from tickle.common.responses.errors import SearchTickersMissingQArgError


#------------------------------------------------------
# Decorator for isQueryUrlRequestParmPresent
#------------------------------------------------------
def verifyRequiredUrlParm(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # if user is not logged in, redirect to login page
        if not isQueryUrlRequestParmPresent():
            return responses.badRequest(SearchTickersMissingQArgError)

        return f(*args, **kwargs)

    return wrap

#------------------------------------------------------
# Checks if the current request provided the required 'q' url parm 
#------------------------------------------------------
def isQueryUrlRequestParmPresent() -> bool:
    query_val = flask.request.args.get('q') or None

    if query_val:
        return True
    else:
        return False





