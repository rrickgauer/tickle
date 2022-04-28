


from tickle.common.domain import models
from tickle.common.domain.enums.watches import PairTypes
from .routines import getProductMap
import json


def getTag(watch: models.Watch) -> str:

    pair_map = getProductMap(watch.pair_type)
    # m = pair_map.get(watch.pair_id)

    print(watch)

    # print(watch.pair_id, watch.pair_type, len(pair_map))
    # print(m)

    map_keys = set(pair_map.keys())
    if watch.pair_id in map_keys:
        print('is in')
    else:
        print('not found')


    # print(m)



