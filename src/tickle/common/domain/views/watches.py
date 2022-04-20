"""
********************************************************************************************

Watch views

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
class ViewWatch:
    id              : UUID        = None
    ticker          : str         = None
    ticker_type     : TickerTypes = None
    ticker_name     : str         = None
    price           : Decimal     = None
    watch_type      : WatchTypes  = None
    watch_type_name : str         = None
    email           : str         = None
    created_on      : datetime    = None
    closed_on       : datetime    = None
