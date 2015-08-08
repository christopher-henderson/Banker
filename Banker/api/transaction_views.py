from api.api_bases import ObjectView, CollectionView
from common.serializers import TransactionSerializer


class TransactionBase:

    SENSITIVE_ATTRIBUTES = frozenset(['account'])
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return self.request.account.transaction_set.all()


class TransactionObjectView(TransactionBase, ObjectView):
    pass


class TransactionCollectionView(TransactionBase, CollectionView):
    pass
