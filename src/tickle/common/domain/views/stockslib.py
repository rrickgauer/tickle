"""
********************************************************************************************

Investpy api response data views

********************************************************************************************
"""

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class StocksApiSearchResponse:
    id_       : int = None #  1174681,
    name      : str = None #  "SentinelOne Inc",
    symbol    : str = None #  "S",
    country   : str = None #  "united states",
    tag       : str = None #  "/equities/sentinelone",
    pair_type : str = None #  "stocks",
    exchange  : str = None #  "NYSE"

@dataclass
class StocksApiInformationResponse:
    last              : float = None # 34.11,
    prevClose         : float = None # 35.38,
    dailyRange        : str   = None # "33.73-35.34",
    revenue           : int   = None # 204810000,
    open              : float = None # 34.83,
    weekRange         : str   = None # "29.3-78.53",
    eps               : float = None # -1.34,
    volume            : int   = None # 2416172,
    marketCap         : int   = None # 9270000000,
    dividend          : str   = None # "N/A(N/A)",
    avgVolume         : int   = None # 4492645,
    ratio             : str   = None # "-",
    beta              : str   = None # "-",
    oneYearReturn     : str   = None # "-",
    sharesOutstanding : int   = None # 271755385,
    nextEarningDate   : str   = None # "29/06/2022"