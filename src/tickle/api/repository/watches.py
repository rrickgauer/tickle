"""
********************************************************************************************

Watches repository

********************************************************************************************
"""

from __future__ import annotations
from uuid import UUID
import pymysql.commands as sql_engine
from pymysql.structs import DbOperationResult
from tickle.common.domain import models

SQL_INSERT = '''
    INSERT INTO 
        Watches (id, ticker, ticker_type, price, watch_type, email)
    VALUES
        (%s, %s, %s, %s, %s, %s);
'''


SQL_SELECT_ALL_OPEN = '''
    SELECT 
        * 
    FROM 
        View_Watches w
    WHERE 
        w.closed_on is null
    ORDER BY 
        ticker_type ASC,
        ticker ASC;
'''

SQL_SELECT = '''
    SELECT
        *
    FROM 
        View_Watches w
    WHERE
        w.id = %s
    LIMIT 
        1;
'''

#------------------------------------------------------
# Insert the watch record into the database
#------------------------------------------------------
def insert(watch: models.Watch) -> DbOperationResult:

    parms = (
        str(watch.id),
        watch.ticker,
        watch.ticker_type.value,
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


def select(watch_id: UUID) -> DbOperationResult:
    parms = (str(watch_id),)
    return sql_engine.select(SQL_SELECT, parms)