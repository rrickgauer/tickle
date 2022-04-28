"""
********************************************************************************************

Enums for watches

********************************************************************************************
"""

from __future__ import annotations
from enum import Enum, unique
from .extended_enums import ExtendedEnum

@unique
class WatchTypes(ExtendedEnum):
    RISE = 1
    DROP = 2


class TickerTypes(Enum):
    STOCKS = 1
    CRYPTO = 2

