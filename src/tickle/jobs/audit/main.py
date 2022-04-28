"""
************************************************************************************

This is the main entry point.

***************************************************************************************
"""

from __future__ import annotations
from tickle.jobs.audit import api_wrapper
from .cliargs import CliArgs
from . import controller
from tickle import stockslib

# parse the command line
cliargs = CliArgs()
cliargs.parse()

# configure the application
controller.configureApplication(cliargs.is_production)


# get a list of watches that need to be closed
open_watches = api_wrapper.getOpenWatches()


# get the prices of the watches

tags = []
for x in open_watches:
    tags.append(x.tag)


prices = stockslib.getPrices(tags)

print(prices)












# # get an email connection
# email_engine = controller.getEmailEngine(cliargs.is_production)
# email_engine.connect()



# for watch in watches_to_close:
    
#     try:
#         email_engine.sendMessage(watch)     # send email to recipient
#         api_wrapper.closeWatch(watch.id)    # close watch in database
#     except Exception as ex:
#         print(ex)

# email_engine.disconnect()
