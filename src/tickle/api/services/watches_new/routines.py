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
from tickle.common.utilities import dumpJson

from tickle.common.structs import BaseReturn

def createNew() -> BaseReturn:
    service_result = BaseReturn(successful=False)

    try:
        model = _getRequestFormData()
    except Exception as ex:
        service_result.error = ex
        return service_result

    # validate the model's properties

    service_result.successful = True
    service_result.data = model

    return service_result



def _getRequestFormData() -> models.Watch2:
    request_data = flask.request.form.to_dict()
    model = _serializeModel(request_data)
    return model


def _serializeModel(watch_dict: dict) -> models.Watch2:
    serializer = serializers.Watch2Serializer(watch_dict)
    return serializer.serialize()


def _validateNewModel(watch: models.Watch2):

    # need to check if the id exists
    s = 3

    


