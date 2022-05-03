"""
********************************************************************************************

Url Prefix: /prices

********************************************************************************************
"""

from __future__ import annotations
import flask
from tickle.api import security
from tickle.common import responses

import tickle.api.services.prices as price_services

# module blueprint
bp_prices = flask.Blueprint('prices', __name__)


#------------------------------------------------------
# GET: /prices?tag=
#
# Get the price of the specified tag
#------------------------------------------------------
@bp_prices.get('')
@security.localEndpoint
@price_services.verifyRequiredUrlParm
def getPrice():
    args  = flask.request.args.to_dict()
    tag   = args.get('tag')
    price = price_services.getPrice(tag)

    if not price:
        return responses.badRequest(f'Could not fetch the price of the specified tag: {tag}')

    return responses.get(price)