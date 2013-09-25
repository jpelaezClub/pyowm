#!/usr/bin/env python

"""
Module containing APIResponseError class
"""

class APIResponseError(Exception):
    """
    Error class that represents HTTP error status codes in OWM web API responses.
    
    :param cause: the message of the error
    :type cause: str
    :returns: a *APIResponseError* instance
    """    
    def __init__(self, message):
        self._message = message
        
    def __str__(self):
        """Redefine __str__ hook for pretty-printing"""
        return 'An error HTTP status code was returned by the OWM API. Reason: %s' % \
            self._message