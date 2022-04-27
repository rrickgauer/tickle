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
bp_watches_new = flask.Blueprint('watches_new', __name__)

#------------------------------------------------------
# POST: /watches
#------------------------------------------------------
@bp_watches_new.post('')
def newWatch():
    return 'created'