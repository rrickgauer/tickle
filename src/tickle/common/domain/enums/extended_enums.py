"""
********************************************************************************************

This is an extended enum class. It provides some additional methods for enums.

values: returns a list of all the values in an enum. 
    For example:

        MyEnum(enum):
            red   = 1
            blue  = 2
            white = 3
        
        MyEnum.values() would return [1, 2, 3]

names: returns a list of all the names in an enum. 
    For example:

        MyEnum(enum):
            red   = 1
            blue  = 2
            white = 3
        
        MyEnum.values() would return ['red', 'blue', 'white']


********************************************************************************************
"""

from __future__ import annotations
from enum import Enum

class ExtendedEnum(Enum):

    @classmethod
    def values(cls) -> list:
        """Get a list of all the enum class values"""
        return list(map(lambda c: c.value, cls))

    @classmethod
    def names(cls) -> list[str]:
        """Get a list of all the enum class names"""
        return list(map(lambda c: c.name, cls))

    
    @classmethod
    def getByKey(cls, key: str) -> Enum | None:
        """Get the enum value that has the specified key"""
        return cls._member_map_.get(key)
