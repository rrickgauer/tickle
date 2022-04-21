"""
********************************************************************************************

Ticker price domain model.

********************************************************************************************
"""

from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from tickle.common.domain.enums.watches import TickerTypes

import typing


@dataclass
class TickerPrice:
    ticker      : str         = None
    price       : Decimal     = None
    ticker_type : TickerTypes = None


# Map of TickerPrices whose keys are the ticker symbol
TickerPriceMap = typing.Dict[str, TickerPrice]