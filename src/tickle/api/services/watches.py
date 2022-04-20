"""
********************************************************************************************

Watches services.

A watch is made up of:
    a stock to keep an eye out on
    a target price
    a watch type (if the price falls or if it rises beyond the watch price)

********************************************************************************************
"""

from __future__ import annotations
from uuid import UUID
import flask
from tickle.common import serializers, utilities, BaseReturn
from tickle.common.domain import models
from tickle.common.domain.enums.watches import TickerTypes
from tickle.common.domain.views.watches import ViewOpenWatchesMaps, ViewWatch, ViewWatchMap, ViewOpenWatchesList
import tickle.api.repository.watches as watches_repo

#------------------------------------------------------
# Create a new watch record from the request data
#------------------------------------------------------
def createNew() -> BaseReturn:
    watch = _getModelFromRequestForm()
    watch.id = utilities.getUUID(False)

    result = BaseReturn(successful=False)
    
    # save the new record
    try:
        _saveModel(watch)
    except Exception as ex:
        result.error = ex
        return result

    # fetch the watch view
    try:
        view = _getView(watch.id)
    except Exception as ex:
        result.error = ex
        return result

    result.successful = True
    result.data = view
    return result


#------------------------------------------------------
# Create a serialized Watch model from the request's form data
#------------------------------------------------------
def _getModelFromRequestForm() -> models.Watch:
    form = flask.request.form.to_dict()
    return serializers.WatchSerializer(form).serialize()

#------------------------------------------------------
# Save the given watch model to the database
#------------------------------------------------------
def _saveModel(watch: models.Watch):
    result = watches_repo.insert(watch)
    
    if not result.successful:
        raise result.error

#------------------------------------------------------
# Get the specified WatchView from the database
#------------------------------------------------------
def _getView(watch_id: UUID) -> ViewWatch | None:
    db_result = watches_repo.select(watch_id)

    if not db_result.successful:
        raise db_result.error

    if not db_result.data:
        return None
    
    serializer = serializers.WatchViewSerializer(db_result.data)
    return serializer.serialize()


#------------------------------------------------------
# Get a dictionary of open watches
# The keys are the tickers 
#------------------------------------------------------
def getOpenWatches() -> ViewOpenWatchesMaps:
    model_list = _getOpenWatchesModelList()
    models_by_ticker_type = _splitModelsByType(model_list)
    watches_dict = _toViewOpenWatchesMaps(models_by_ticker_type)

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
# Split the 1 dimensional list of models into their ticker types (stocks or crypto)
#------------------------------------------------------
def _splitModelsByType(open_watches: list[ViewWatch]) -> ViewOpenWatchesList:
    stocks_list = []
    crypto_list = []

    for watch in open_watches:
        if watch.ticker_type == TickerTypes.CRYPTO:
            crypto_list.append(watch)
        else:
            stocks_list.append(watch)

    result = ViewOpenWatchesList(
        stocks = stocks_list,
        crypto = crypto_list
    )

    return result

#------------------------------------------------------
# Transform the specified ViewOpenWatchesList into a ViewOpenWatchesMaps
#------------------------------------------------------
def _toViewOpenWatchesMaps(models_by_ticker_type: ViewOpenWatchesList) -> ViewOpenWatchesMaps:
    result = ViewOpenWatchesMaps(
        stocks = _toViewWatchMap(models_by_ticker_type.stocks),
        crypto = _toViewWatchMap(models_by_ticker_type.crypto),
    )

    return result

#------------------------------------------------------
# Transform the given list of Watches into a dictionary of tickers as keys
#------------------------------------------------------
def _toViewWatchMap(models_list: list[ViewWatch]) -> ViewWatchMap:
    watches_dict = {}

    for model in models_list:
        if model.ticker in watches_dict:
            watches_dict[model.ticker].append(model)
        else:
            watches_dict.setdefault(model.ticker, [model])
        
    return watches_dict