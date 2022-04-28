"""
************************************************************************************

This is the main entry point.

***************************************************************************************
"""

from __future__ import annotations
from tickle.jobs.audit import api_wrapper
from .cliargs import CliArgs
from . import controller

# parse the command line
cliargs = CliArgs()
cliargs.parse()

# configure the application
controller.configureApplication(cliargs.is_production)


# get a list of watches that need to be closed
open_watches = api_wrapper.getOpenWatches()
print(open_watches)

# need to build a list of tags for each of the open watches


# then, pass that list of tags to the stockslib to fetch the prices



















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
