from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import ListCreateViewAPI, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import authentication, permissions

    

class ObjectView(RetrieveUpdateDestroyAPIView, Queryable):
    authentication_classes = (authentication.TokenAuthentication,)
    parser_classes = (JSONParser,)

class AccountView(ObjectView, Queryable):
    pass


class ClassificationView(ObjectView, Queryable):
    pass


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
