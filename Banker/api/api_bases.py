from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import (
    ListCreateViewAPI,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import authentication

from common.models import *
from common.serializers import *


class QueryableAPIView:

    SENSITIVE_ATTRIBUTES = frozenset()
    authentication_classes = (authentication.TokenAuthentication,)
    parser_classes = (JSONParser,)

    def find(self, query):
        raise NotImplementedError()

    def filter(self, query):
        raise NotImplementedError()

    def sanitize(self, query):
        if self.SENSITIVE_ATTRIBUTES:
            return {
                k: v for k, v in query.items()
                if k not in self.SENSITIVE_ATTRIBUTES
            }
        else:
            return query

    def response_or_404(self, query_result, many=False):
        response = Response()
        if query_result is None:
            response.status_code = 404
        else:
            response.data = self.serializer_class(query_result, many=many)
        return response


class ObjectView(QueryableAPIView, RetrieveUpdateDestroyAPIView):

    def find(self, query):
        try:
            query_result = self.get_queryset().get(**self.sanitize(query))
        except ObjectDoesNotExist:
            query_result = None
        return self.response_or_404(query_result)

    def get(self, request):
        return self.find(request.GET)


class CollectionsView(QueryableAPIView, ListCreateViewAPI):

    def filter(self, query):
        query_result = self.get_query_set().filter(**self.sanitize(query))
        return response_or_404(query_result)

    def get(self, request):
        return self.filter(request.GET, many=True)
