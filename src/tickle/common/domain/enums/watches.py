"""
********************************************************************************************

Enums for watches

********************************************************************************************
"""

from __future__ import annotations
from enum import Enum, unique

from .extended_enums import ExtendedEnum

@unique
class WatchTypes(Enum):
    RISE = 1
    DROP = 2


class TickerTypes(Enum):
    STOCKS = 1
    CRYPTO = 2


@unique
class PairTypes(ExtendedEnum):
    INDICES      = 1
    STOCKS       = 2
    ETFS         = 3
    FUNDS        = 4
    COMMODITIES  = 5
    CURRENCIES   = 6
    CRYPTOS      = 7
    BONDS        = 8
    CERTIFICATES = 9
    FXFUTURES    = 10


@unique
class PairTypesText(str, ExtendedEnum):
    INDICES      = 'indices'
    STOCKS       = 'stocks'
    ETFS         = 'etfs'
    FUNDS        = 'funds'
    COMMODITIES  = 'commodities'
    CURRENCIES   = 'currencies'
    CRYPTOS      = 'cryptos'
    BONDS        = 'bonds'
    CERTIFICATES = 'certificates'
    FXFUTURES    = 'fxfutures'

