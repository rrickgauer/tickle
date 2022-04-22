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
# Display home page
#------------------------------------------------------
@bp_home.route('')
def homePage():
    return flask.render_template('index.html')