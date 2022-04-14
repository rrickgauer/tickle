"""
**********************************************************************************************

This module handles generating flask responses.

A flask response is a tuple that consists of:
    - the body
    - return code

**********************************************************************************************
"""

from http import HTTPStatus
import flask


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
# Resource was successfully DELETED
#----------------------------------------------------------
def deleted(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.NO_CONTENT)

#----------------------------------------------------------
# Client error
#----------------------------------------------------------
def badRequest(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.BAD_REQUEST)

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
def internal_error(output=None) -> flask.Response:
    return _standardReturn(output, HTTPStatus.INTERNAL_SERVER_ERROR)


#----------------------------------------------------------
# The standard return logic for all the methods
#----------------------------------------------------------
def _standardReturn(output, response_code: HTTPStatus) -> flask.Response:
    if isinstance(output, type(None)):
        return ('', response_code)

    try:
        output_string = flask.jsonify(output)
    except Exception as ex:
        output_string = ''

    return (output_string, response_code)




