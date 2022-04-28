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
        Watches2 (id, pair_type, pair_id, price, watch_type, email)
    VALUES
        (%s, %s, %s, %s, %s, %s);
'''



#------------------------------------------------------
# Insert the watch record into the database
#------------------------------------------------------
def insert(watch: models.Watch) -> DbOperationResult:
    parms = (
        str(watch.id),
        watch.pair_type.value,
        watch.pair_id,
        watch.price,
        watch.watch_type.value,
        watch.email,
    )

    return sql_engine.modify(SQL_INSERT, parms)