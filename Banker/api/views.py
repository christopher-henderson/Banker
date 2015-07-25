import re
from functools import wraps

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from common.models import *


def none_if_does_not_exist(function):
    @wraps(function)
    def wrapper(cls, *args, **kwargs):
        try:
            return function(cls, *args, **kwargs)
        except ObjectDoesNotExist:
            return None
    return wrapper


class Queryable:
    
    ATTRIBUTE = '[_a-zA-Z][_a-zA-Z0-9]*'
    VALUE = '.+'
    VALID_QUERY = re.compile('{ATTR}={VAL}(&{ATTR}={VAL})*'.format(ATTR=ATTRIBUTE, VAL=VALUE))
    KWARG_ASSIGNMENT  = re.compile(r'(?<!\\)=')
    KWARG_DELIMITER = re.compile(r'(?<!\\)&')

    @classmethod
    @none_if_does_not_exist
    def parse(cls, query_set, query, plural=False):
        if not cls.valid_syntax(query):
            raise Exception()
        parsed_query = cls.sanitize(cls.tokenize(query))
        return query_set.filter(**parsed_query) if plural else query_set.get(**parsed_query) 

    @staticmethod
    def tokenize(query):
        '''Tokenize query into a dictionary.'''
        return {k: v for k, v in (KWARG_ASSIGNMENT.split(kwargs) for kwargs in KWARG_DELIMITER.split(query))}

    @classmethod
    def valid_syntax(cls, query):
        return bool(cls.VALID_QUERY.match(query))

    @classmethod
    def sanitize(cls, query):
        raise NotImplementedError()


class AuthenticatedAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication)


class AccountView(AuthenticatedAPIView, Queryable):
    
    @classmethod
    def sanitize(cls, query):
        return query


class ClassificationView(AuthenticatedAPIView, Queryable):
    
    @classmethod
    def sanitize(cls, query):
        return query


class TransactionView(AuthenticatedAPIView, Queryable):
    
    @classmethod
    def sanitize(cls, query):
        return query


class TimeView(AuthenticatedAPIView, Queryable):
    
    @classmethod
    def sanitize(cls, query):
        return query


class BillView(AuthenticatedAPIView, Queryable):
    
    @classmethod
    def sanitize(cls, query):
        return query


class VendorView(AuthenticatedAPIView, Queryable):
    
    @classmethod
    def sanitize(cls, query):
        return query


class ItemView(AuthenticatedAPIView, Queryable):
    
    @classmethod
    def sanitize(cls, query):
        return query


class StatisticView(AuthenticatedAPIView, Queryable):
    
    @classmethod
    def sanitize(cls, query):
        return query
