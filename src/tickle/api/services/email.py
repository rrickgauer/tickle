

from __future__ import annotations
import flask
import yagmail

# from tickle.api.globals import app_config

from tickle.api.globals import getConfig




def sendEmail():

    config = getConfig()

    yag = yagmail.SMTP(
        user = flask.current_app.config.get('EMAIL_USERNAME'),
        password = flask.current_app.config.get('EMAIL_PASSWORD'),
    )

    contents = 'this was sent from python'

    return 'hi'
    # return yag.send('rrickgauer1@gmail.com', 'testing', contents)
