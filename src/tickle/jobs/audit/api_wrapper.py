"""
************************************************************************************

Wrapper routines for the api.

***************************************************************************************
"""

from __future__ import annotations
import requests
from tickle.common import serializers
from tickle.common.domain.views.watches import ViewWatch
from tickle.common.config import configs

API_URL_PREFIX = configs.Production.URL_API
API_URL_ENDPOINT = '/v1/internal/audit'





#------------------------------------------------------
# Get a list of watches that need to be closed from the API
#------------------------------------------------------
def getWatchesToClose() -> list[ViewWatch]:
    api_response_data = requests.get(_getApiUrl()).json().get('data')
    watches_to_close = []

    for record in api_response_data:
        serializer = serializers.WatchViewSerializer(record)
        watches_to_close.append(serializer.serialize())

    return watches_to_close



def _getApiUrl() -> str:
    return f'{API_URL_PREFIX}{API_URL_ENDPOINT}'