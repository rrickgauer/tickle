"""
********************************************************************************************

Watches services.

********************************************************************************************
"""

from __future__ import annotations
import flask

from tickle.common.domain import models
from tickle.common.domain.enums.watches import PairTypes
from tickle.common import serializers
from tickle.common.domain.views import stockslib
from tickle.common.utilities import dumpJson

from tickle import stockslib

from tickle.common.structs import BaseReturn

def createNew() -> BaseReturn:
    service_result = BaseReturn(successful=False)

    try:
        model = _getRequestFormData()
    except Exception as ex:
        service_result.error = ex
        return service_result

    # validate the model's properties
    if not _validateNewModel(model):
        service_result.error = "pair_id does not exist"
        return service_result


    service_result.successful = True
    service_result.data = model

    return service_result

#------------------------------------------------------
# get the request's form data 
#------------------------------------------------------
def _getRequestFormData() -> models.Watch2:
    request_data = flask.request.form.to_dict()
    model = _serializeModel(request_data)
    return model

#------------------------------------------------------
# serialzie the given dictionary into a watch model
#------------------------------------------------------
def _serializeModel(watch_dict: dict) -> models.Watch2:
    serializer = serializers.Watch2Serializer(watch_dict)
    return serializer.serialize()

#------------------------------------------------------
# make sure that the specified pair_id is supported with investpy
#------------------------------------------------------
def _validateNewModel(watch: models.Watch2) -> bool:
    product_map = stockslib.getProductMap(watch.pair_type)
    product = product_map.get(watch.pair_id) or None

    if not product:
        return False

    return True





