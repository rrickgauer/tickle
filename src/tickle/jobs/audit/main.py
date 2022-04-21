"""
************************************************************************************

This is the main entry point.

***************************************************************************************
"""

from __future__ import annotations
from .cliargs import CliArgs
from . import controller

# parse the command line
cliargs = CliArgs()
cliargs.parse()

# configure the application
controller.configureApplication(cliargs.is_production)











