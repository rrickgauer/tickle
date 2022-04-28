"""
************************************************************************************

Wrapper routines for the api.

***************************************************************************************
"""

from __future__ import annotations
from enum import Enum
import requests
from tickle.common import serializers
from tickle.common.domain.models.watches import Watch
from tickle.common.domain.views.watches import ViewWatch
from tickle.common.config import configs
from tickle.common.utilities import dumpJson

API_URL_PREFIX = configs.Production.URL_API

class ApiEndpoints(str, Enum):
    AUDIT = '/internal/audit'
    WATCHES = '/watches'


#------------------------------------------------------
# Fetch a list of open watches from the api
#------------------------------------------------------
def getOpenWatches() -> list[Watch]:
    api_response = _requestOpenWatches()
    dumpJson(api_response)

    watches = []
    
    for watch_record in api_response:
        serializer = serializers.Watch2Serializer(watch_record)
        watches.append(serializer.serialize())

    return watches

def _requestOpenWatches() -> list[dict]:
    api_response = requests.get(
        url     = _getApiUrl(ApiEndpoints.WATCHES),
        headers = _getCustomHeaders(),
    )

    if not api_response.ok:
        raise ConnectionError(api_response.text)
    
    return api_response.json().get('data')

#------------------------------------------------------
# Get a list of watches that need to be closed from the API
#------------------------------------------------------
def getWatchesToClose() -> list[ViewWatch]:
    api_response_data = _getRequestData()
    watches_to_close = []

    for record in api_response_data:
        serializer = serializers.WatchViewSerializer(record)
        watches_to_close.append(serializer.serialize())

    return watches_to_close


#------------------------------------------------------
# Get the open watches from the api
#------------------------------------------------------
def _getRequestData():
    url = _getApiUrl(ApiEndpoints.AUDIT)
    response = requests.get(url, headers=_getCustomHeaders())

    if not response.ok:
        raise Exception(str(response.text))

    try:
        data = response.json().get('data')
    except Exception as ex:
        print(ex)
        data = []
    
    return data


#------------------------------------------------------
# Create a custom headers dictionary
#------------------------------------------------------
def _getCustomHeaders() -> dict:
    custom_headers = {
        configs.Production.SECURITY_HEADER_KEY: configs.Production.SECURITY_HEADER_VALUE,
    }

    return custom_headers


#------------------------------------------------------
# Tell the api to close the specified watch
#------------------------------------------------------
def closeWatch(watch_id) -> requests.Response:
    url = f'{_getApiUrl(ApiEndpoints.WATCHES)}/{watch_id}'
    return requests.delete(url, headers=_getCustomHeaders())


def _getApiUrl(endpoint: ApiEndpoints) -> str:
    return f'{API_URL_PREFIX}{endpoint.value}'