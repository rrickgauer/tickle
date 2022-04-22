"""
********************************************************************************************

Home page services

********************************************************************************************
"""

from __future__ import annotations
from dataclasses import dataclass
from functools import wraps
import flask

from tickle.common.domain.enums.watches import TickerTypes, WatchTypes


@dataclass
class HomePageUrlValues:
    ticker_type: TickerTypes = None
    ticker     : str         = None
    price      : float       = None
    watch_type : WatchTypes  = None


def getUrlValues() -> HomePageUrlValues:
    url_args = flask.request.view_args

    url_values = HomePageUrlValues(
        ticker_type = url_args.get('ticker_type') or None,
        ticker      = url_args.get('ticker') or None,
        price       = url_args.get('price') or None,
        watch_type  = url_args.get('watch_type') or None,
    )

    return url_values