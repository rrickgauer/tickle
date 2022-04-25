"""
********************************************************************************************

Url Prefix: /new

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.common.domain.enums.watches import TickerTypes, WatchTypes
from tickle.gui.services import home_page as homepage_services


# module blueprint
bp_new = flask.Blueprint('new', __name__)

#------------------------------------------------------
# Get ticker information
#------------------------------------------------------
@bp_new.route('')
def getTickerInfo():
    return flask.render_template('new/form-sections/ticker.html')


#------------------------------------------------------
# Get price info
#------------------------------------------------------
@bp_new.route('<ticker_type:ticker_type>/<string:ticker>')
def getPriceAndWatchType(ticker_type: TickerTypes, ticker: str):
    return flask.render_template('new/form-sections/price.html')