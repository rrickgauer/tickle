"""
************************************************************************************

This is the main entry point.

***************************************************************************************
"""

from __future__ import annotations

from tickle.jobs.audit import api_wrapper
from .cliargs import CliArgs
from . import controller
from tickle.common.email.messenger import Messenger

# parse the command line
cliargs = CliArgs()
cliargs.parse()

# configure the application
controller.configureApplication(cliargs.is_production)

# get an email connection
email_engine = controller.getEmailEngine(cliargs.is_production)
email_engine.connect()

# get a list of watches that need to be closed
watches_to_close = api_wrapper.getWatchesToClose()

# email the account saying that the price has broken its barrier
for watch in watches_to_close:
    email_engine.sendMessage(watch)


# close the watches in the database















