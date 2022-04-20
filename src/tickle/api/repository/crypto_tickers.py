"""
********************************************************************************************

Crypto_Tickers repository

********************************************************************************************
"""

from __future__ import annotations
import pymysql.commands as sql_engine
from pymysql.structs import DbOperationResult


SEARCH_STORED_PROCEDURE = 'Search_Crypto_Tickers'

# Call the crypto search stored procedure
def search(query: str) -> DbOperationResult:
    parms = [query]
    return sql_engine.proc(SEARCH_STORED_PROCEDURE, parms)






