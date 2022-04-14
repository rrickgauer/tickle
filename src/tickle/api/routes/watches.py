"""
********************************************************************************************

Url Prefix: /watches

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.api.services import watches as watch_services


# module blueprint
bp_watches = flask.Blueprint('watches', __name__)

#------------------------------------------------------
# POST: /watches
#------------------------------------------------------
@bp_watches.post('')
def newWatch():
    return watch_services.responses_POST()

        



