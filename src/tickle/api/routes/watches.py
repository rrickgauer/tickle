"""
********************************************************************************************

Url Prefix: /watches

********************************************************************************************
"""

from __future__ import annotations
from uuid import UUID
import flask
from tickle.api import security
from tickle.common import responses
from tickle.common.responses.errors import BaseError, ErrorCodes
from tickle.api.services import watches_new as watch_services

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


#------------------------------------------------------
# GET: /watches
#
# Get all open watches
#------------------------------------------------------
@bp_watches.get('')
@security.localEndpoint
def get():
    try:
        watches = watch_services.getOpenWatches()
    except RuntimeError as ex:
        return (str(ex), 500)

    return responses.get(watches)



#------------------------------------------------------
# GET: /watches
#
# Get all open watches
#------------------------------------------------------
@bp_watches.delete('<uuid:watch_id>')
@security.localEndpoint
def delete(watch_id: UUID):
    
    return 'deleted'

    return responses.get(watches)