"""
********************************************************************************************

Email services

********************************************************************************************
"""

from __future__ import annotations
import yagmail
from tickle.common.domain.enums.watches import WatchTypes
from tickle.common.domain.models import Watch

CONTENTS_TEMPLATE = 'The price of {symbol} has {movement} to {price}.'
SUBJECT           = 'Tickle price alert'
SUBJECT_TEMPLATE  = '{symbol} price alert'


# Create the email body message
def getContents(watch: Watch):
    if watch.watch_type == WatchTypes.DROP:
        movement_text = 'dropped'
    else:
        movement_text = 'rose'
    
    contents = CONTENTS_TEMPLATE.format(
        symbol = watch.symbol,
        movement = movement_text,
        price    = watch.price,
    )

    return contents



class Messenger:

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._email_engine: yagmail.SMTP = None
    
    def connect(self):
        self._email_engine = yagmail.SMTP(
            user = self._username,
            password = self._password,
        )

    def disconnect(self):
        self._email_engine.close()
    

    def sendPriceAlertMessage(self, watch: Watch):
        contents = getContents(watch)

        try:
            send_result = self._email_engine.send(
                to       = watch.email,
                subject  = SUBJECT_TEMPLATE.format(symbol=watch.symbol),
                contents = contents,
            )

            return True

        except Exception as ex:
            print(ex)
            return False

        

