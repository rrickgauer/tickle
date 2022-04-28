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

# #------------------------------------------------------
# # Get ticker information
# #------------------------------------------------------
# @bp_new.route('')
# def getTickerInfo():
#     payload = dict(
#         url_values = homepage_services.getUrlValues(),
#     )

#     return flask.render_template('new/form-sections/ticker.html', data=payload)


# #------------------------------------------------------
# # Get price info
# #------------------------------------------------------
# @bp_new.route('<ticker_type:ticker_type>/<string:ticker>')
# def getPriceAndWatchType(ticker_type: TickerTypes, ticker: str):

#     payload = dict(
#         url_values = homepage_services.getUrlValues(),
#     )

#     return flask.render_template('new/form-sections/price.html', data=payload)


# #------------------------------------------------------
# # Get the email
# #------------------------------------------------------
# @bp_new.route('<ticker_type:ticker_type>/<ticker>/<price>/<watch_type:watch_type>')
# def getEmail(ticker_type: TickerTypes, ticker, price, watch_type: WatchTypes):

#     payload = dict(
#         url_values = homepage_services.getUrlValues(),
#     )

#     return flask.render_template('new/form-sections/email.html', data=payload)
