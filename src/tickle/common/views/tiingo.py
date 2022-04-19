"""
********************************************************************************************

Tiingo api response data views

********************************************************************************************
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass
class TickerResponse:
    ticker            : str      = None  #:"AAPL",
    timestamp         : datetime = None  #:"2019-01-30T10:33:38.186520297-05:00",
    quoteTimestamp    : datetime = None  #:"2019-01-30T10:33:38.186520297-05:00"
    lastSaleTimeStamp : datetime = None  #:"2019-01-30T10:33:34.176037579-05:00",
    last              : Decimal  = None  #:162.37,
    lastSize          : int      = None  #:100,
    tngoLast          : Decimal  = None  #:162.33,
    prevClose         : Decimal  = None  #:154.68,
    open              : Decimal  = None  #:161.83,
    high              : Decimal  = None  #:163.25,
    low               : Decimal  = None  #:160.38,
    mid               : Decimal  = None  #:162.67,
    volume            : int      = None  #:0,
    bidSize           : int      = None  #:100,
    bidPrice          : Decimal  = None  #:162.34,
    askSize           : Decimal  = None  #:100,
    askPrice          : Decimal  = None  #:163.0

