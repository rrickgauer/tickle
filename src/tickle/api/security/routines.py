from __future__ import annotations
import flask
from functools import wraps



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
    request_ip = _getRequestIpAddress()
    host_ip = _getHostIpAddress()

    if request_ip == host_ip:
        return True
    else:
        return False


def _getRequestIpAddress() -> str:
    request_ip = flask.request.remote_addr.split(':')[0]
    return request_ip


def _getHostIpAddress() -> str:
    host_ip = flask.request.host.split(':')[0]
    return host_ip

