"""
**********************************************************************************************

This module contains all the serializers.
A serializer transforms a dictionary into a domain model.

**********************************************************************************************
"""

from __future__ import annotations
from dataclasses import dataclass
import datetime
from decimal import Decimal
from typing import Any
from tickle.common.domain import models
from tickle.common.domain.enums.watch_types import WatchTypes
from tickle.common.views import tiingo


#------------------------------------------------------
# Parse the given datetime string into a python datetime/date object
#
# Args:
#   datetime_module: either the datetime.datetime module or the datetime.date module (both have the fromisoformat function)
#   date_string: the date string to parse
#------------------------------------------------------
def parseIsoDatetime(datetime_module, date_string: str=None) -> datetime.datetime | str | None:    
    try:
        result = datetime_module.fromisoformat(date_string)
    except Exception as e:
        result = date_string
    
    return result

def serializeDecimal(decimal_val) -> Decimal | None | Any:
    try:
        result = Decimal(decimal_val)
    except:
        result = decimal_val
    
    return result

#------------------------------------------------------
# Base serializer class
#------------------------------------------------------
class SerializerBase:
    DomainModel: dataclass = object

    #------------------------------------------------------
    # Constructor
    #
    # Args:
    #   - dictionary: a dict of the data to serialize into the Domain Model
    #   - domain_model: an instance of the class' DomainModel or None
    #------------------------------------------------------
    def __init__(self, dictionary: dict, domain_model = None):
        self.dictionary = dictionary
        
        # if the given domain_model is not null, set the object's domain_model field to it
        # otherwise, call the contructor of the class' DomainModel
        self.domain_model = domain_model or self.DomainModel()

    #------------------------------------------------------
    # Serialize the object's dictionary into the sub-class' domain model
    #------------------------------------------------------
    def serialize(self) -> dataclass:
        model = self.domain_model

        # get a list of all the Model's attributes
        model_keys = list(model.__annotations__.keys())

        # if the dict's key is an attribute in the model, copy over the value
        for key, value in self.dictionary.items():
            if not key in model_keys:
                continue
            elif not value:
                setattr(model, key, None)
            else:
                setattr(model, key, value or None)

        return model




#------------------------------------------------------
# Watch serializer
#------------------------------------------------------
class WatchSerializer(SerializerBase):
    DomainModel = models.Watch

    def serialize(self) -> models.Watch:
        model = super().serialize()

        try:
            model.watch_type = WatchTypes(int(model.watch_type))
        except:
            model.watch_type = None

        return model


#------------------------------------------------------
# Watch serializer
#------------------------------------------------------
class TickerResponseSerializer(SerializerBase):
    DomainModel = tiingo.TickerResponse

    def serialize(self) -> models.Watch:
        model: tiingo.TickerResponse = super().serialize()

        # serialize the potential datetimes
        model.timestamp         = parseIsoDatetime(datetime.datetime, model.timestamp)
        model.quoteTimestamp    = parseIsoDatetime(datetime.datetime, model.quoteTimestamp)
        model.lastSaleTimeStamp = parseIsoDatetime(datetime.datetime, model.lastSaleTimeStamp)  

        # serialize the potential decimal types
        model.last      = serializeDecimal(model.last)
        model.tngoLast  = serializeDecimal(model.tngoLast)
        model.prevClose = serializeDecimal(model.prevClose)
        model.open      = serializeDecimal(model.open)
        model.high      = serializeDecimal(model.high)
        model.low       = serializeDecimal(model.low)
        model.mid       = serializeDecimal(model.mid)
        model.bidPrice  = serializeDecimal(model.bidPrice)
        model.askSize   = serializeDecimal(model.askSize)
        model.askPrice  = serializeDecimal(model.askPrice)

        return model


#------------------------------------------------------
# Watch serializer
#------------------------------------------------------
class CryptoSymbolApiResponseSerializer(SerializerBase):
    DomainModel = tiingo.CryptoSymbolApiResponse

    def serialize(self) -> tiingo.CryptoSymbolApiResponse:
        return super().serialize()

    
