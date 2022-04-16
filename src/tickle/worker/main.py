"""
**********************************************************************************************

This is the main entrypoint to run.

**********************************************************************************************
"""

from __future__ import annotations

import pymysql
from tickle.common.config import configs
import tickle.api.repository.watches as watches_repo



pymysql.credentials.USER     = configs.ConfigBase.DB_USER
pymysql.credentials.PASSWORD = configs.ConfigBase.DB_PASSWORD
pymysql.credentials.DATABASE = configs.ConfigBase.DB_NAME
pymysql.credentials.HOST     = configs.ConfigBase.DB_HOST


data = watches_repo.selectAllOpen()

print(data)








