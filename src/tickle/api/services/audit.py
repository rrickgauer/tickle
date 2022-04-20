"""
********************************************************************************************

Watch records auditing services

********************************************************************************************
"""

from __future__ import annotations
import tickle.api.repository.watches as watches_repo
from tickle.common import serializers
from tickle.common.domain.enums.watches import WatchTypes
from tickle.common.domain.views.watches import ViewWatch
from tickle.common.domain.views.tiingo import TickerResponse

#------------------------------------------------------
# Get a dictionary of open watches
# The keys are the tickers 
#------------------------------------------------------
def getOpenWatches() -> dict[str, list[ViewWatch]]:
    model_list = _getOpenWatchesModelList()
    watches_dict = _toTickerDict(model_list)

    return watches_dict

#------------------------------------------------------
# Get a list of Watch models that are open
#------------------------------------------------------
def _getOpenWatchesModelList() -> list[ViewWatch]:
    models = []
    
    for d in watches_repo.selectAllOpen().data:
        serializer = serializers.WatchViewSerializer(d)
        model = serializer.serialize()
        models.append(model)

    return models

#------------------------------------------------------
# Transform the given list of Watches into a dictionary of tickers as keys
#------------------------------------------------------
def _toTickerDict(models_list: list[ViewWatch]) -> dict[str, list[ViewWatch]]:
    watches_dict = {}

    for model in models_list:
        if model.ticker in watches_dict:
            watches_dict[model.ticker].append(model)
        else:
            watches_dict.setdefault(model.ticker, [model])
        
    return watches_dict


#------------------------------------------------------
# Run price checks on watches
# Returns a list of watches to close
#------------------------------------------------------
def runPriceChecks(open_watches: dict[str, list[ViewWatch]], stock_prices: dict[str, list[TickerResponse]]) -> list[ViewWatch]:
    watchs_to_confirm = []

    for stock_symbol, ticker_response in stock_prices.items():
        # get all the watches for the current ticker symbol
        watches_for_this_symbol = open_watches.get(stock_symbol) or []

        # get a list of ones that need to be closed
        confirm_these_watches   = _runPriceCheckForSymbol(watches_for_this_symbol, ticker_response)

        # add it to the result list
        watchs_to_confirm.extend(confirm_these_watches)

    return watchs_to_confirm

#------------------------------------------------------
# Get a list of watches that have the specified ticker that need to be closed
#------------------------------------------------------
def _runPriceCheckForSymbol(open_watches: list[ViewWatch], ticker_response: TickerResponse):
    current_stock_price = ticker_response.last
    watches_to_confirm = []

    for open_watch in open_watches:
        
        if open_watch.watch_type == WatchTypes.RISE:
            price_check_routine_delegate = _priceCheckForRise
        else:
            price_check_routine_delegate = _priceCheckForDrop

        if price_check_routine_delegate(open_watch, current_stock_price):
            watches_to_confirm.append(open_watch)
    
    return watches_to_confirm



def _priceCheckForRise(watch: ViewWatch, current_price) -> bool:
    return current_price > watch.price


def _priceCheckForDrop(watch: ViewWatch, current_price) -> bool:
    return current_price < watch.price





