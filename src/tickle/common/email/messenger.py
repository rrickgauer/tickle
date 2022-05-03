"""
********************************************************************************************

Email services

********************************************************************************************
"""

from __future__ import annotations
import yagmail
from tickle.common.domain.models import Watch
from .messages import templates
from .messages.formatters import formatCloseWatchPriceAlert


class MessengerBase:

    def __init__(self, username: str, password: str):
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

    def send(self):
        raise NotImplementedError

    def _send(self, destination, subject, contents):
        send_result = self._email_engine.send(
            to       = destination,
            subject  = subject,
            contents = contents,
        )

        return send_result



class CloseWatchMessenger(MessengerBase):

    def send(self, watch: Watch):
        return self._send(
            destination = watch.email,
            subject     = templates.SUBJECT_TEMPLATE.format(symbol=watch.symbol),
            contents    = formatCloseWatchPriceAlert(watch),
        )





