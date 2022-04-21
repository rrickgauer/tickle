"""
************************************************************************************

Controller for the jobs

***************************************************************************************
"""

from __future__ import annotations
import pymysql
from tickle.common.config import configs
from . import api_wrapper

#------------------------------------------------------
# Initialize some variables using the configuration values
#------------------------------------------------------
def setConfigOptions(is_production: bool):
    config = _getConfigClass(is_production)

    _setPymysqlCredentials(config)
    _setUrls(config)
    
#------------------------------------------------------
# Get the appropriate configuration class
#------------------------------------------------------
def _getConfigClass(is_production: bool) -> configs.ConfigBase:
    if is_production:
        configuration = configs.Production
    else:
        configuration = configs.Dev

    return configuration

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



