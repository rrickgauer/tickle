"""
************************************************************************************

This is the main entry point.

***************************************************************************************
"""

from __future__ import annotations
import json

from tickle.common.domain import models
from tickle.common.domain.enums.watches import WatchTypes
from tickle.jobs.audit import api_wrapper
from .cliargs import CliArgs
from . import routines
from tickle import stockslib

# parse the command line
cliargs = CliArgs()
cliargs.parse()

# configure the application
routines.configureApplication(cliargs.is_production)


# get a list of watches that need to be closed
open_watches = api_wrapper.getOpenWatches()

# get the prices of the watches
tags = []
for x in open_watches:
    tags.append(x.tag)

prices = stockslib.getPrices(tags)

watches_to_close: list[models.Watch] = []

for open_watch in open_watches:
    current_price = prices.get(open_watch.tag).last
    
    if open_watch.watch_type == WatchTypes.RISE:
        if current_price >= open_watch.price:
            watches_to_close.append(open_watch)
    else:
        if current_price <= open_watch.price:
            watches_to_close.append(open_watch)

# get an email connection
email_engine = routines.getEmailEngine(cliargs.is_production)
email_engine.connect()

for watch in watches_to_close:
    try:
        print(email_engine.sendPriceAlertMessage(watch))     # send email to recipient
        api_wrapper.closeWatch(watch.id)    # close watch in database
    except Exception as ex:
        print(ex)

email_engine.disconnect()
