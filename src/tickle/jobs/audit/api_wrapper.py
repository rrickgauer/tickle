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
from tickle.common.config import configs

API_URL_PREFIX = configs.Production.URL_API

class ApiEndpoints(str, Enum):
    AUDIT = '/internal/audit'
    WATCHES = '/watches'

#------------------------------------------------------
# Fetch a list of open watches from the api
#------------------------------------------------------
def getOpenWatches() -> list[Watch]:
    api_response = _requestOpenWatches()
    watches = []
    
    for watch_record in api_response:
        serializer = serializers.WatchSerializer(watch_record)
        watches.append(serializer.serialize())

    return watches

def _requestOpenWatches() -> list[dict]:
    
    api_url = _getApiUrl(ApiEndpoints.WATCHES)

    api_response = requests.get(
        url     = api_url,
        headers = _getCustomHeaders(),
    )

    if not api_response.ok:
        raise ConnectionError(api_response.text)
    
    return api_response.json().get('data')

#------------------------------------------------------
# Tell the api to close the specified watch
#------------------------------------------------------
def closeWatch(watch_id) -> requests.Response:
    url = f'{_getApiUrl(ApiEndpoints.WATCHES)}/{watch_id}'
    return requests.delete(url, headers=_getCustomHeaders())

#------------------------------------------------------
# Create a custom headers dictionary
#------------------------------------------------------
def _getCustomHeaders() -> dict:
    custom_headers = {
        configs.Production.SECURITY_HEADER_KEY: configs.Production.SECURITY_HEADER_VALUE,
    }

    return custom_headers


def _getApiUrl(endpoint: ApiEndpoints) -> str:
    return f'{API_URL_PREFIX}{endpoint.value}'