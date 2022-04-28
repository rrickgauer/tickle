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

SQL_CLOSE_WATCH = '''
    UPDATE 
        Watches2 w
    SET 
        w.closed_on = NOW()
    WHERE 
        w.id = %s
    LIMIT 1;
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


# Fetch all the open watches from the database
def selectAllOpen() -> DbOperationResult:
    return sql_engine.selectAll(SQL_SELECT_ALL_OPEN)


def closeWatch(watch_id: UUID) -> DbOperationResult:
    parms = (str(watch_id),)
    return sql_engine.modify(SQL_CLOSE_WATCH, parms)

    