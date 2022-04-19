"""
********************************************************************************************

Watches repository

********************************************************************************************
"""

from __future__ import annotations
import pymysql.commands as sql_engine
from pymysql.structs import DbOperationResult
from tickle.common.domain import models

SQL_INSERT = '''
    INSERT INTO 
        Watches (id, ticker, price, watch_type, email)
    VALUES
        (%s, %s, %s, %s, %s);
'''


SQL_SELECT_ALL_OPEN = '''
    SELECT 
        * 
    FROM 
        View_Watches w
    WHERE 
        w.closed_on is null
    ORDER BY 
        ticker ASC
    LIMIT 10;
'''




#------------------------------------------------------
# Insert the watch record into the database
#------------------------------------------------------
def insert(watch: models.Watch) -> DbOperationResult:
    parms = (
        str(watch.id),
        watch.ticker,
        watch.price,
        watch.watch_type.value,
        watch.email,
    )

    return sql_engine.modify(SQL_INSERT, parms)

#------------------------------------------------------
# Get all the open watch records from the database
#------------------------------------------------------
def selectAllOpen() -> DbOperationResult:
    return sql_engine.selectAll(SQL_SELECT_ALL_OPEN)
