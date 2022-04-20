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
import flask
from tickle.common import serializers
from tickle.common import responses
from tickle.common.domain import models
from tickle.common import utilities
import tickle.api.repository.watches as watches_repo

#------------------------------------------------------
# Response to a POST request and create a new watch record
#------------------------------------------------------
def responses_POST() -> flask.Response:
    watch = getModelFromRequestForm()
    watch.id = utilities.getUUID(False)
    
    try:
        saveModel(watch)
    except:
        return responses.internalError()

    return responses.created(watch)

#------------------------------------------------------
# Create a serialized Watch model from the request's form data
#------------------------------------------------------
def getModelFromRequestForm() -> models.Watch:
    form = flask.request.form.to_dict()
    return serializers.WatchSerializer(form).serialize()

#------------------------------------------------------
# Save the given watch model to the database
#------------------------------------------------------
def saveModel(watch: models.Watch):
    result = watches_repo.insert(watch)
    
    if not result.successful:
        print(result.error)
        raise result.error





