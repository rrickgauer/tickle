"""
********************************************************************************************

This module formats template strings.

********************************************************************************************
"""

from tickle.common.domain.enums.watches import WatchTypes
from tickle.common.domain.models import Watch
from tickle.common.utilities import formatFloatToCurrency
from . import templates


# Create the email body message
def formatCloseWatchPriceAlert(watch: Watch):
    if watch.watch_type == WatchTypes.DROP:
        movement_text = 'dropped'
    else:
        movement_text = 'rose'
    
    contents = templates.PRICE_ALERT_TEMPLATE.format(
        symbol   = watch.symbol,
        movement = movement_text,
        price    = formatFloatToCurrency(watch.price),
    )

    return contents