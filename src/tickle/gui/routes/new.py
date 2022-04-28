"""
********************************************************************************************

Url Prefix: /new

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.common.domain.enums.watches import WatchTypes
from tickle.gui.services import home_page as homepage_services


# module blueprint
bp_new = flask.Blueprint('new', __name__)

#------------------------------------------------------
# Get ticker information
#------------------------------------------------------
@bp_new.route('')
def new():
    return flask.render_template('new/new-watch.html')

