"""
************************************************************************************

This is class for the command line argument for the audit job.

***************************************************************************************
"""

from __future__ import annotations
import argparse

#------------------------------------------------------
# Symbolic constants for the cli arg descriptions
#------------------------------------------------------
class ArgumentDescriptions:
    ARGUMENT_PARSER = "Perform an audit on open watches"
    DEVELOPMENT_FLAG = "Flag indicating to run in development mode."


class CliArgs:

    #------------------------------------------------------
    # Constructor
    #------------------------------------------------------
    def __init__(self):
        self._parser = argparse.ArgumentParser(description=ArgumentDescriptions.ARGUMENT_PARSER)
        self._args = None
        self.is_production = True

    #------------------------------------------------------
    # Parse the command line arguments
    #------------------------------------------------------
    def parse(self):
        self._addArguments()
        self._args = self._parser.parse_args()
        self._assignObjectValues()


    #------------------------------------------------------
    # Add all the arguments to the parser
    #------------------------------------------------------
    def _addArguments(self):
        self._parser.add_argument('-d', '--development', action="store_false", help=ArgumentDescriptions.DEVELOPMENT_FLAG)

    #------------------------------------------------------
    # Set the object's property values to the ones specified in the cli arguments
    #------------------------------------------------------
    def _assignObjectValues(self):
        self.is_production = self._args.development
    
    

        