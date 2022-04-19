"""
********************************************************************************************

Crypto_Tickers repository

********************************************************************************************
"""

from __future__ import annotations
import pymysql.commands as sql_engine
from pymysql.structs import DbOperationResult
from pymysql.connection import ConnectionPrepared
from tickle.common.domain import models
from tickle.common.views.tiingo import CryptoSymbolApiResponse


SQL_INSERT = '''
    INSERT IGNORE INTO 
        Crypto_Tickers (ticker, name, baseCurrency, quoteCurrency)
    VALUES
        (%s, %s, %s, %s);
'''


def insertBatch(crypto_tickers: list[CryptoSymbolApiResponse]) -> DbOperationResult:
    return _insert2(crypto_tickers)
    
    parms = _getInsertBatchParms(crypto_tickers)
    sub_list = []

    last_index = 0

    for i, parm_tuple in enumerate(parms):

        if i % 100 == 0 and i > 0:
            last_index = i
            print(i)
            sub_list = parms[i:i+100]
            sql_engine.modifyBatch(SQL_INSERT, sub_list)

    sub_list = parms[last_index:]
    sql_engine.modifyBatch(SQL_INSERT, sub_list)

    return True



    # print(parms)
    return sql_engine.modifyBatch(SQL_INSERT, parms)



def _insert2(crypto_tickers: list[CryptoSymbolApiResponse]):
    result = DbOperationResult(successful=True)
    parms = _getInsertBatchParms(crypto_tickers)
    
    db = ConnectionPrepared()

    sub_list = []

    db.connect()
    cursor = db.getCursor()
    last_index = 0

    try:

        for i, parm_tuple in enumerate(parms):

            if i % 100 != 0 or i == 0:
                continue
        
            last_index = i
            print(i)
            sub_list = parms[i:i+100]
            # sql_engine.modifyBatch(SQL_INSERT, sub_list)
            cursor.executemany(SQL_INSERT, sub_list)


        # get the last sub list
        sub_list = parms[last_index:]
        # sql_engine.modifyBatch(SQL_INSERT, sub_list)
        cursor.executemany(SQL_INSERT, sub_list)
        
        db.commit()
        
        result.data = cursor.rowcount
    except Exception as e:
        result.successful = False
        result.data = None
        result.error = e
    finally:
        db.close()
    
    return result




def _insertSubList(cursor, sub_list):
    cursor.executemany(SQL_INSERT, sub_list)




    


def _getInsertBatchParms(crypto_tickers: list[CryptoSymbolApiResponse]) -> list[tuple]:
    parms_list = []

    for crypto_ticker in crypto_tickers:
        parms = (
            crypto_ticker.ticker,
            crypto_ticker.name,
            crypto_ticker.baseCurrency,
            crypto_ticker.quoteCurrency,
        )

        parms_list.append(parms)
    
    return parms_list

