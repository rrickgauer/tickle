"""
********************************************************************************************

Enums for watches

********************************************************************************************
"""

from __future__ import annotations
from enum import Enum


class WatchTypes(Enum):
    RISE = 1
    DROP = 2


class TickerTypes(Enum):
    STOCKS = 1
    CRYPTO = 2