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
from tickle.common.domain.enums.watches import WatchTypes
from tickle.common.domain.enums.watches import TickerTypes
from tickle.common.domain.views import tiingo
from tickle.common.domain.views.watches import ViewWatch
from tickle.common.domain.views import stockslib


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

        try:
            model.ticker_type = TickerTypes(int(model.ticker_type))
        except:
            model.ticker_type = None

        return model


#------------------------------------------------------
# Watch view serializer
#------------------------------------------------------
class WatchViewSerializer(WatchSerializer):
    DomainModel = ViewWatch

    def serialize(self) -> ViewWatch:
        return super().serialize()

#------------------------------------------------------
# Watch serializer
#------------------------------------------------------
class TickerResponseSerializer(SerializerBase):
    DomainModel = tiingo.StockTickerPrice

    def serialize(self) -> models.Watch:
        model: tiingo.StockTickerPrice = super().serialize()

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
# Crypto symbol api response serializer
#------------------------------------------------------
class CryptoSymbolApiResponseSerializer(SerializerBase):
    DomainModel = tiingo.CryptoSymbolApiResponse

    def serialize(self) -> tiingo.CryptoSymbolApiResponse:
        return super().serialize()

#------------------------------------------------------
# Stock search api response serializer
#------------------------------------------------------
class StockSearchApiResponseSerializer(SerializerBase):
    DomainModel = tiingo.StockSearchApiResponse

    def serialize(self) -> tiingo.StockSearchApiResponse:
        return super().serialize()


#------------------------------------------------------
# CryptoTickerPriceTopOfBookData serializer
#------------------------------------------------------
class CryptoTickerPriceTopOfBookDataSerializer(SerializerBase):
    DomainModel = tiingo.CryptoTickerPriceTopOfBookData

    def serialize(self) -> tiingo.CryptoTickerPriceTopOfBookData:
        model: tiingo.CryptoTickerPriceTopOfBookData = super().serialize()

        # model.lastPrice        = serializeDecimal(model.lastPrice)
        # model.askPrice         = serializeDecimal(model.askPrice)
        # model.bidSize          = serializeDecimal(model.bidSize)
        # model.lastSizeNotional = serializeDecimal(model.lastSizeNotional)
        # model.askSize          = serializeDecimal(model.askSize)
        # model.lastSize         = serializeDecimal(model.lastSize)
        # model.bidPrice         = serializeDecimal(model.bidPrice)

        model.quoteTimestamp = parseIsoDatetime(model.quoteTimestamp)
        model.lastSaleTimestamp = parseIsoDatetime(model.lastSaleTimestamp)

        return model

#------------------------------------------------------
# Crypto price api response serializer
#------------------------------------------------------
class CryptoTickerPriceSerializer(SerializerBase):
    DomainModel = tiingo.CryptoTickerPrice

    def serialize(self) -> tiingo.CryptoTickerPrice:
        model: tiingo.CryptoTickerPrice = super().serialize()

        top_of_book_dict = model.topOfBookData[0]
        serializer = CryptoTickerPriceTopOfBookDataSerializer(top_of_book_dict)
        model.topOfBookData = serializer.serialize()

        return model



class StocksLibSearchResponseSerializer(SerializerBase):
    DomainModel = stockslib.StocksApiSearchResponse

    def serialize(self) -> stockslib.StocksApiSearchResponse:
        return super().serialize()
