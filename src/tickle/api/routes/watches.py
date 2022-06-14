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
from tickle.api.services import watches as watch_services

# module blueprint
bp_watches = flask.Blueprint('watches', __name__)

#------------------------------------------------------
# POST: /watches
#
# Create a new watch
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
# DELETE: /watches/:watch_id
#
# Delete (close) the specified watch record
#------------------------------------------------------
@bp_watches.delete('<uuid:watch_id>')
@security.localEndpoint
def delete(watch_id: UUID):
    if not watch_services.closeWatch(watch_id):
        return ('', 404)
    
    return responses.deleted()