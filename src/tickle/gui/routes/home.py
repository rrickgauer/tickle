"""
********************************************************************************************

Url Prefix: /home

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.common.domain.enums.watches import TickerTypes, WatchTypes
from tickle.gui.services import home_page as homepage_services


# module blueprint
bp_home = flask.Blueprint('home', __name__)

#------------------------------------------------------
# Select ticker type
#------------------------------------------------------
@bp_home.route('')
def getTickerType():
    url_values = homepage_services.getUrlValues()

    payload = dict(
        url_values = url_values
    )

    return flask.render_template('home/form-sections/ticker-type.html', data=payload)

#------------------------------------------------------
# Ticker search
#------------------------------------------------------
@bp_home.route('<ticker_type:ticker_type>')
def getTicker(ticker_type: TickerTypes):
    url_values = homepage_services.getUrlValues()

    payload = dict(
        url_values = url_values
    )
    return flask.render_template('home/form-sections/ticker-search.html', data=payload)


#------------------------------------------------------
# Get the price and watch type
#------------------------------------------------------
@bp_home.route('<ticker_type:ticker_type>/<string:ticker>')
def getPriceAndWatchType(ticker_type: TickerTypes, ticker: str):
    url_values = homepage_services.getUrlValues()

    payload = dict(
        url_values = url_values
    )
    return flask.render_template('home/form-sections/price.html', data=payload)


#------------------------------------------------------
# Get the email
#------------------------------------------------------
@bp_home.route('<ticker_type:ticker_type>/<ticker>/<price>/<watch_type:watch_type>')
def getEmail(ticker_type: TickerTypes, ticker, price, watch_type: WatchTypes):
    url_values = homepage_services.getUrlValues()

    payload = dict(
        url_values = url_values
    )

    return flask.render_template('home/form-sections/email.html', data=payload)

    
