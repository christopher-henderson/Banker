from api.api_bases import ObjectView, CollectionsView
from common.serializers import TransactionSerializer

class TransactionBase:

    serializer_class = TransactionSerializer
    SENSITIVE_ATTRIBUTES = frozenset(['account']) 

    def get_queryset(self):
        return self.request.account.transaction_set.all()  

class TransactionObjectView(TransactionBase, ObjectView):
    pass


class TransactionCollectionsView(TransactionBase, CollectionsView):
    pass