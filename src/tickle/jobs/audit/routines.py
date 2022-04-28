"""
************************************************************************************

Controller for the jobs

***************************************************************************************
"""

from __future__ import annotations
import pymysql
from tickle.common.config import configs
from . import api_wrapper
from tickle.common.email.messenger import Messenger

#------------------------------------------------------
# Initialize some variables using the configuration values
#------------------------------------------------------
def configureApplication(is_production: bool):
    config = _getConfigClass(is_production)
    _setPymysqlCredentials(config)
    _setUrls(config)

#------------------------------------------------------
# Set the database credentials 
#------------------------------------------------------
def _setPymysqlCredentials(config: configs.ConfigBase):
    pymysql.credentials.USER     = config.DB_USER
    pymysql.credentials.PASSWORD = config.DB_PASSWORD
    pymysql.credentials.DATABASE = config.DB_NAME
    pymysql.credentials.HOST     = config.DB_HOST


#------------------------------------------------------
# Set the api urls
#------------------------------------------------------
def _setUrls(config: configs.ConfigBase):
    api_wrapper.API_URL_PREFIX = config.URL_API

#------------------------------------------------------
# Get an email engine object
#------------------------------------------------------
def getEmailEngine(is_production: bool) -> Messenger:
    config = _getConfigClass(is_production)
    email_engine = Messenger(config.EMAIL_USERNAME, config.EMAIL_PASSWORD)
    return email_engine


#------------------------------------------------------
# Get the appropriate configuration class
#------------------------------------------------------
def _getConfigClass(is_production: bool) -> configs.ConfigBase:
    if is_production:
        configuration = configs.Production
    else:
        configuration = configs.Dev

    return configuration