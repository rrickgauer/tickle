"""
********************************************************************************************

Url Prefix: /watches

********************************************************************************************
"""

from __future__ import annotations
import flask
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
        result = watch_services.createNewWatch()
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

        



