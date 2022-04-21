"""
********************************************************************************************

Watch domain model

********************************************************************************************
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from tickle.common.domain.enums.watches import WatchTypes
from tickle.common.domain.enums.watches import TickerTypes

@dataclass
class Watch:
    id          : UUID        = None
    ticker_type : TickerTypes = None
    ticker      : str         = None
    price       : Decimal     = None
    watch_type  : WatchTypes  = None
    email       : str         = None
    created_on  : datetime    = datetime.now()
    closed_on   : datetime    = None