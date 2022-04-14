"""
**********************************************************************************************

This module handles generating flask responses.

A flask response is a tuple that consists of:
    - the body
    - return code

**********************************************************************************************
"""

from dataclasses import dataclass
from http import HTTPStatus
import flask
from .errors import BaseError

@dataclass
class StandardResponse:
    data: any = None


#----------------------------------------------------------
# Resource successfully GET - the normal return
#----------------------------------------------------------
def get(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.OK)

#----------------------------------------------------------
# Resource was successfully UPDATED
#----------------------------------------------------------
def updated(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.OK)

#----------------------------------------------------------
# Resource was successfully CREATED
#----------------------------------------------------------
def created(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.CREATED)



#----------------------------------------------------------
# The standard return logic for all the methods
#----------------------------------------------------------
def _standardReturn(output, response_code: HTTPStatus) -> tuple:
    result = StandardResponse()
    
    if isinstance(output, type(None)):
        return (flask.jsonify(result), response_code)

    result.data = output
    
    try:
        output_string = flask.jsonify(result)
    except Exception as ex:
        output_string = ''

    return (output_string, response_code)


#----------------------------------------------------------
# Resource was successfully DELETED
#----------------------------------------------------------
def deleted(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.NO_CONTENT)


#----------------------------------------------------------
# Not found error
#----------------------------------------------------------
def notFound(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.NOT_FOUND)

#----------------------------------------------------------
# Forbidden
#----------------------------------------------------------
def forbidden(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.FORBIDDEN)

#----------------------------------------------------------
# Forbidden
#----------------------------------------------------------
def internalError(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.INTERNAL_SERVER_ERROR)

#----------------------------------------------------------
# Client error
#----------------------------------------------------------
def badRequest(error: BaseError) -> flask.Response:
    return _badReturn(error, HTTPStatus.BAD_REQUEST)


def _badReturn(error: BaseError, response_code: HTTPStatus) -> tuple:
    payload = dict(
        error = error,
    )

    output = flask.jsonify(payload)

    return (output, response_code.value)

