"""
********************************************************************************************

Watches services

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.common import responses, serializers
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
        return responses.internal_error()

    return responses.created(watch)

#------------------------------------------------------
# Create a serialized Watch model from the request's form data
#------------------------------------------------------
def getModelFromRequestForm() -> models.Watch:
    form = flask.request.form.to_dict()
    return serializers.WatchSerializer(form).serialize()


def saveModel(watch: models.Watch):
    result = watches_repo.insert(watch)
    
    if not result.successful:
        print(result.error)
        raise result.error





