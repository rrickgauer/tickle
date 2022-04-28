"""
********************************************************************************************

Watches services.

********************************************************************************************
"""

from __future__ import annotations
from uuid import UUID
import flask
from tickle.common.domain import models
from tickle.common import serializers
from tickle.common.utilities import getUUID
from tickle.common.structs import BaseReturn
import tickle.api.repository.watches as watches_repo

#------------------------------------------------------
# Create a new watch
#------------------------------------------------------
def createNew() -> BaseReturn:
    service_result = BaseReturn(successful=False)

    # retrive and serialize the request's form data
    try:
        model = _getRequestFormData()
        model.id = getUUID(False)
    except Exception as ex:
        service_result.error = ex
        return service_result

    # validate the model's properties
    try:
        _validateNewModel(model)
    except ValueError as ex:
        service_result.error = ex
        return service_result

    # insert it into the database
    try:
        _saveWatch(model)
    except RuntimeError as ex:
        service_result.error = ex
        return service_result

    # all good... 
    service_result.successful = True
    service_result.data = model

    return service_result

#------------------------------------------------------
# get the request's form data 
#------------------------------------------------------
def _getRequestFormData() -> models.Watch:
    request_data = flask.request.form.to_dict()
    model = _serializeModel(request_data)

    return model

#------------------------------------------------------
# serialzie the given dictionary into a watch model
#------------------------------------------------------
def _serializeModel(watch_dict: dict) -> models.Watch:
    serializer = serializers.WatchSerializer(watch_dict)
    return serializer.serialize()

#------------------------------------------------------
# make sure that the specified pair_id is supported with investpy
#------------------------------------------------------
def _validateNewModel(watch: models.Watch):
    if _checkForNull(watch):
        raise ValueError("Missing a required field in the request. The required fields are: 'pair_type', 'pair_id', 'price', 'watch_type', 'email'.")

#------------------------------------------------------
# Checks if any of the required Watch properties are null 
#------------------------------------------------------
def _checkForNull(watch: models.Watch) -> bool:
    
    required_properties = [
        watch.tag,
        watch.price,
        watch.watch_type,
        watch.email,
    ]

    if None in required_properties:
        return True
    else:
        return False

#------------------------------------------------------
# Save the watch to the database
#------------------------------------------------------
def _saveWatch(watch: models.Watch):
    db_result = watches_repo.insert(watch)

    if not db_result.successful:
        raise RuntimeError(str(db_result.error))

    return db_result


#------------------------------------------------------
# Get all open watches
#------------------------------------------------------
def getOpenWatches() -> list[models.Watch]:
    db_result = watches_repo.selectAllOpen()

    if not db_result.successful:
        raise RuntimeError(str(db_result.error))
    
    watches = db_result.data or []
    return watches

#------------------------------------------------------
# Close the specified watch
#
# Returns a bool:
#    true: all good
#    false: watch does not exist
#------------------------------------------------------
def closeWatch(watch_id: UUID) -> bool:
    result = watches_repo.closeWatch(watch_id)

    if not result.successful:
        raise result.error

    if result.data == 1:
        return True
    else:
        return False
    

