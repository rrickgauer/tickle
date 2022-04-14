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
    GENERAL = auto()


@dataclass
class BaseError:
    code   : ErrorCodes = None
    message: str        = None


DefaultError = BaseError(
    code    = ErrorCodes.GENERAL,
    message = 'Default error'
)




