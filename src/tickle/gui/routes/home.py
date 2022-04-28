"""
********************************************************************************************

Url Prefix: /

********************************************************************************************
"""

from __future__ import annotations
import flask


# module blueprint
bp_home = flask.Blueprint('home', __name__)

#------------------------------------------------------
# Get ticker information
#------------------------------------------------------
@bp_home.route('')
def homePage():
    return flask.redirect(flask.url_for('new.new'))