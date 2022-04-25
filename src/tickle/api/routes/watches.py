"""
********************************************************************************************

Url Prefix: /watches

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.api import security
from tickle.api.services import watches as watch_services
from tickle.common import responses
from tickle.common.responses.errors import BaseError, ErrorCodes

# module blueprint
bp_watches = flask.Blueprint('watches', __name__)

#------------------------------------------------------
# POST: /watches
#------------------------------------------------------
@bp_watches.post('')
def newWatch():
    try:
        result = watch_services.createNew()
    except Exception as ex:
        return responses.internalError(str(ex))
    
    if not result.successful:
        error = BaseError(
            code    = ErrorCodes.CREATE_NEW_WATCH,
            message = str(result.error),
        )

        return responses.badRequest(error)

    if not result.data:
        return responses.notFound()
    
    return responses.created(result.data)


#------------------------------------------------------
# GET: /watches
#------------------------------------------------------
@bp_watches.get('')
@security.localEndpoint
def getOpenWatches():
    open_watches = watch_services.getOpenWatches()
    return responses.get(open_watches)


#------------------------------------------------------
# Delete a watch (close it)
#------------------------------------------------------
@bp_watches.delete('<uuid:watch_id>')
@security.localEndpoint
def deleteWatch(watch_id):
    watch_services.closeWatch(watch_id)
    return responses.deleted()



