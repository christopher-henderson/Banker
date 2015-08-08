from api.api_bases import ObjectView, CollectionView
from common.serializers import AccountSerializer


class AccountBase:

    SENSITIVE_ATTRIBUTES = frozenset(['account'])
    serializer_class = AccountSerializer

    def get_queryset(self):
        return self.request.account


class AccountObjectView(AccountBase, ObjectView):
    pass


class AccountCollectionView(AccountBase, CollectionView):
    pass
