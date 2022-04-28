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
        Watches2 (id, tag, price, watch_type, email)
    VALUES
        (%s, %s, %s, %s, %s);
'''

SQL_SELECT_ALL_OPEN = '''
    SELECT 
        *
    FROM 
        Watches2 w
    WHERE
        w.closed_on IS NULL
    ORDER BY 
        created_on DESC;
'''



#------------------------------------------------------
# Insert the watch record into the database
#------------------------------------------------------
def insert(watch: models.Watch) -> DbOperationResult:
    parms = (
        str(watch.id),
        watch.tag,
        watch.price,
        watch.watch_type.value,
        watch.email,
    )

    return sql_engine.modify(SQL_INSERT, parms)



def selectAllOpen() -> DbOperationResult:
    return sql_engine.selectAll(SQL_SELECT_ALL_OPEN)