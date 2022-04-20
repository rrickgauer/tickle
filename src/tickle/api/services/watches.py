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
from tickle.common import serializers
from tickle.common.domain import models
from tickle.common.domain.views.watches import ViewWatch
from tickle.common import utilities
import tickle.api.repository.watches as watches_repo
from tickle.common import BaseReturn

#------------------------------------------------------
# Create a new watch record from the request data
#------------------------------------------------------
def createNewWatch() -> BaseReturn:
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


# Get the specified WatchView from the database
def _getView(watch_id: UUID) -> ViewWatch | None:
    db_result = watches_repo.select(watch_id)

    if not db_result.successful:
        raise db_result.error

    if not db_result.data:
        return None
    
    serializer = serializers.WatchViewSerializer(db_result.data)
    return serializer.serialize()
