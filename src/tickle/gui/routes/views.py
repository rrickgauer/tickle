"""
********************************************************************************************

Url Prefix: /

These are the routes for the html pages.

********************************************************************************************
"""

from __future__ import annotations
import flask


# module blueprint
bp_views = flask.Blueprint('views', __name__)

#------------------------------------------------------
# Home page
# tickle.com
#------------------------------------------------------
@bp_views.route('')
def home():
    return flask.render_template('home/index.html')

#------------------------------------------------------
# Create a new watch
# tickle.com/new
#------------------------------------------------------
@bp_views.route('new')
def newWatch():
    return flask.render_template('new/index.html')

#------------------------------------------------------
# Create a new watch
# tickle.com/about
#------------------------------------------------------
@bp_views.route('about')
def about():
    return flask.render_template('about/index.html')