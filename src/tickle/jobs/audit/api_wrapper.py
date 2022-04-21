"""
************************************************************************************

Wrapper routines for the api.

***************************************************************************************
"""

from __future__ import annotations
from enum import Enum
import requests
from tickle.common import serializers
from tickle.common.domain.views.watches import ViewWatch
from tickle.common.config import configs

API_URL_PREFIX = configs.Production.URL_API

class ApiEndpoints(str, Enum):
    AUDIT = '/v1/internal/audit'
    WATCHES = '/v1/watches'

#------------------------------------------------------
# Get a list of watches that need to be closed from the API
#------------------------------------------------------
def getWatchesToClose() -> list[ViewWatch]:
    api_response_data = requests.get(_getApiUrl(ApiEndpoints.AUDIT)).json().get('data')
    watches_to_close = []

    for record in api_response_data:
        serializer = serializers.WatchViewSerializer(record)
        watches_to_close.append(serializer.serialize())

    return watches_to_close


#------------------------------------------------------
# Tell the api to close the specified watch
#------------------------------------------------------
def closeWatch(watch_id) -> requests.Response:
    url = f'{_getApiUrl(ApiEndpoints.WATCHES)}/{watch_id}'
    return requests.delete(url)

def _getApiUrl(endpoint: ApiEndpoints) -> str:
    return f'{API_URL_PREFIX}{endpoint.value}'