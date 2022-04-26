from __future__ import annotations
import flask
from functools import wraps
from tickle.common.utilities import getConfig

#------------------------------------------------------
# Decorator for verify_authorization_credentials
#------------------------------------------------------
def localEndpoint(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not isRequestLocal():
            flask.abort(403)
        return f(*args, **kwargs)
    return wrap

def isRequestLocal():
    return True
    config = getConfig()
    request_header_value = flask.request.headers.get(config.SECURITY_HEADER_KEY, 'nope')

    if request_header_value == config.SECURITY_HEADER_VALUE:
        return True
    else:
        return False


