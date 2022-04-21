

import requests

from tickle.common.utilities import dumpJson
from tickle.common import serializers


url = 'http://10.0.0.82:5010/v1/internal/audit'

open_watches = []

data = requests.get(url).json().get('data')

for api_response_dict in data:
    serializer = serializers.WatchViewSerializer(api_response_dict)
    open_watches.append(serializer.serialize())



dumpJson(open_watches)











