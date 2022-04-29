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
def notFound(output=None) -> tuple:
    # return _standardReturn(, HTTPStatus.NOT_FOUND)
    return ('', HTTPStatus.NOT_FOUND)

#----------------------------------------------------------
# Forbidden
#----------------------------------------------------------
def forbidden(output=None) -> tuple:
    return ('', HTTPStatus.FORBIDDEN)
    # return _standardReturn('', HTTPStatus.FORBIDDEN)

#----------------------------------------------------------
# Forbidden
#----------------------------------------------------------
def internalError(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.INTERNAL_SERVER_ERROR)

#----------------------------------------------------------
# Client error
#----------------------------------------------------------
def badRequest(output=None) -> flask.Response:
    if not output:
        return ('', HTTPStatus.BAD_REQUEST.value)

    result = dict(
        error = output,
    )
    
    return (flask.jsonify(result), HTTPStatus.BAD_REQUEST.value)

    



