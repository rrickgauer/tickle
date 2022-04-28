"""
********************************************************************************************

Url Prefix: /watches

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.api import security

from tickle.common import responses
from tickle.common.responses.errors import BaseError, ErrorCodes

from tickle.api.services.watches_new import routines as watch_services

# module blueprint
bp_watches = flask.Blueprint('watches_new', __name__)

#------------------------------------------------------
# POST: /watches
#------------------------------------------------------
@bp_watches.post('')
def newWatch():

    result = watch_services.createNew()

    if not result.successful:
        return (str(result.error), 400)
    
    return responses.created(result.data)