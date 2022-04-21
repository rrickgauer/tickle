
"""
********************************************************************************************

Watch records auditing services

********************************************************************************************
"""

from __future__ import annotations
from tickle.common.domain.enums.watches import WatchTypes
from tickle.common.domain.views.watches import ViewWatch
from tickle.common.domain.views.watches import ViewWatchMap
from tickle.common.domain import models
from tickle.api.services import tickerlib

class BaseAuditor:

    def __init__(self, open_watches_map: ViewWatchMap):
        self.open_watches_map = open_watches_map
        self.ticker_symbols = list(open_watches_map.keys())
        self.stock_prices = self._getTickerPrices()

    
    def _getTickerPrices(self):
        pass

    #------------------------------------------------------
    # Run price checks on watches
    # Returns a list of watches to close
    #------------------------------------------------------
    def runPriceChecks(self) -> list[ViewWatch]:
        watchs_to_confirm = []

        for stock_symbol, ticker_response in self.stock_prices.items():
            # get all the watches for the current ticker symbol
            watches_for_this_symbol = self.open_watches_map.get(stock_symbol) or []

            # get a list of ones that need to be closed
            confirm_these_watches   = self._runPriceCheckForSymbol(watches_for_this_symbol, ticker_response)

            # add it to the result list
            watchs_to_confirm.extend(confirm_these_watches)

        return watchs_to_confirm

    #------------------------------------------------------
    # Get a list of watches that have the specified ticker that need to be closed
    #------------------------------------------------------
    def _runPriceCheckForSymbol(self, open_watches: list[ViewWatch], ticker_price: models.TickerPrice):
        current_stock_price = ticker_price.price
        watches_to_confirm = []

        for open_watch in open_watches:
            # determine which qualifier routine to use as a callback
            if open_watch.watch_type == WatchTypes.RISE:
                price_check_routine_delegate = self._priceCheckForRise  
            else:
                price_check_routine_delegate = self._priceCheckForDrop  

            # utilize the callback, if it returns true then the watch should be closed
            if price_check_routine_delegate(open_watch, current_stock_price):
                watches_to_confirm.append(open_watch)
        
        return watches_to_confirm


    # check if the current price is > that the watch price
    def _priceCheckForRise(self, watch: ViewWatch, current_price) -> bool:
        return current_price > watch.price

    # check if the current price is < than the watch price
    def _priceCheckForDrop(self, watch: ViewWatch, current_price) -> bool:
        return current_price < watch.price



class StocksAuditor(BaseAuditor):

    def _getTickerPrices(self):
        return tickerlib.prices.getStockPrices(self.ticker_symbols)
