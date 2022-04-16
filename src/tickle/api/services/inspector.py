"""
********************************************************************************************

ticker inspector services

********************************************************************************************
"""

from __future__ import annotations

import tickle.api.repository.watches as watches_repo
from tickle.common import serializers
from tickle.common.domain import models

def getOpenWatches() -> dict[str, list]:
    model_list = _getOpenWatchesModelList()
    watches_dict = _toTickerDict(model_list)

    return watches_dict


# Get a list of Watch models that are open
def _getOpenWatchesModelList() -> list[models.Watch]:
    models = []
    
    for d in watches_repo.selectAllOpen().data:
        serializer = serializers.WatchSerializer(d)
        model = serializer.serialize()
        models.append(model)

    return models


def _toTickerDict(models_list: list[models.Watch]) -> dict[str, list[models.Watch]]:
    watches_dict = {}

    for model in models_list:
        if model.ticker in watches_dict:
            watches_dict[model.ticker].append(model)
        else:
            watches_dict.setdefault(model.ticker, [model])
        
    return watches_dict