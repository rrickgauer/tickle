from __future__ import annotations
from tickle.common.config import configs
from tickle.common.config.base import ConfigBase
import flask


def getConfig() -> ConfigBase:
    if flask.current_app.env == "production":
        return configs.Production()
    else:
        return configs.Dev()
