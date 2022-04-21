"""
**********************************************************************************************

This module handles generating flask responses.

A flask response is a tuple that consists of:
    - the body
    - return code

**********************************************************************************************
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto

class ErrorCodes(Enum):
    GENERAL                     = auto()
    MISSING_TICKER_SEARCH_Q_ARG = auto()
    CREATE_NEW_WATCH            = auto()


@dataclass
class BaseError:
    code   : ErrorCodes = None
    message: str        = None


DefaultError = BaseError(
    code    = ErrorCodes.GENERAL,
    message = 'Default error'
)

SearchTickersMissingQArgError = BaseError(
    code    = ErrorCodes.MISSING_TICKER_SEARCH_Q_ARG,
    message = 'Missing the required "q" url parameter',
)


CreateNewWatchError = BaseError(
    code = ErrorCodes.CREATE_NEW_WATCH,
    message = None
)


