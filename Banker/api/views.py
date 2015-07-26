from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import ListCreateViewAPI, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import authentication, permissions

from common.models import *
from common.serializers import *


class Queryable:

    SENSITIVE_ATTRIBUTES = frozenset([])

    @classmethod
    def find(cls, query_set, query):
        try:
            return query_set.get(**cls.sanitize(query))
        except ObjectDoesNotExist:
            return None

    @classmethod
    def filter(cls,  query_set, query):
        return query_set.filter(**cls.sanitize(query))

    @classmethod
    def sanitize(cls, query):
        return {k: v for k, v in query.items() if k not in cls.SENSITIVE_ATTRIBUTES}
    

class CollectionsView(ListCreateViewAPI, Queryable):
    authentication_classes = (authentication.TokenAuthentication,)
    parser_classes = (JSONParser,)

class ObjectView(RetrieveUpdateDestroyAPIView, Queryable):
    authentication_classes = (authentication.TokenAuthentication,)
    parser_classes = (JSONParser,)

class AccountView(ObjectView, Queryable):
    pass


class ClassificationView(ObjectView, Queryable):
    pass


class TransactionView(ObjectView, Queryable):
    
    serializer_class = TransactionSerializer
    SENSITIVE_ATTRIBUTES = frozenset(['account'])

    def get(self, request):
        query = request.GET
        query_set = request.user.account.transaction_set.all()
        query_result = {
            'FIND': self.find(query_set, query),
            'FILTER': self.filter(query_set, query)
        }



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
