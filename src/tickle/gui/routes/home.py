"""
********************************************************************************************

Url Prefix: /home

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.common.domain.enums.watches import TickerTypes, WatchTypes

# module blueprint
bp_home = flask.Blueprint('home', __name__)

#------------------------------------------------------
# Select ticker type
#------------------------------------------------------
@bp_home.route('')
def getTickerType():
    return flask.render_template('home/form-sections/ticker-type.html')

#------------------------------------------------------
# Ticker search
#------------------------------------------------------
@bp_home.route('<ticker_type:ticker_type>')
def getTicker(ticker_type: TickerTypes):
    return flask.render_template('home/form-sections/ticker-search.html')


#------------------------------------------------------
# Get the price and watch type
#------------------------------------------------------
@bp_home.route('<ticker_type:ticker_type>/<string:ticker>')
def getPriceAndWatchType(ticker_type: TickerTypes, ticker: str):
    return flask.render_template('home/form-sections/price.html')


#------------------------------------------------------
# Get the email
#------------------------------------------------------
@bp_home.route('<ticker_type:ticker_type>/<ticker>/<price>/<watch_type:watch_type>')
def getEmail(ticker_type: TickerTypes, ticker, price, watch_type: WatchTypes):
    # data = dict(
    #     ticker_type = ticker_type,
    #     ticker = ticker,
    #     price = price,
    #     watch_type = watch_type,
    # )

    # return flask.jsonify(data)

    return flask.render_template('home/form-sections/email.html')

    
