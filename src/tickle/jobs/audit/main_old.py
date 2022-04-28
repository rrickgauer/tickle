"""
************************************************************************************

This is the main entry point.

***************************************************************************************
"""

from __future__ import annotations
from tickle.jobs.audit import api_wrapper
from .cliargs import CliArgs
from . import routines

# parse the command line
cliargs = CliArgs()
cliargs.parse()

# configure the application
routines.configureApplication(cliargs.is_production)

# get an email connection
email_engine = routines.getEmailEngine(cliargs.is_production)
email_engine.connect()

# get a list of watches that need to be closed
watches_to_close = api_wrapper.getWatchesToClose()

for watch in watches_to_close:
    
    try:
        email_engine.sendPriceAlertMessage(watch)     # send email to recipient
        api_wrapper.closeWatch(watch.id)    # close watch in database
    except Exception as ex:
        print(ex)

email_engine.disconnect()
