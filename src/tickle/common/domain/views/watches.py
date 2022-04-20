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

from typing import Dict, List



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


@dataclass
class ViewOpenWatchesList:
    stocks: list[ViewWatch] = None
    crypto: list[ViewWatch] = None


# typedef
ViewWatchMap = Dict[str, List[ViewWatch]]

@dataclass 
class ViewOpenWatchesMaps:
    stocks: ViewWatchMap = None
    crypto: ViewWatchMap = None
