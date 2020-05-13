from rest_framework import serializers
from .models import OrderStatementModel 
from currency.models import UserWallet, ForeignCurrencyWallet
from currency.serializers import UserWalletSerializer, ForeignWalletCurrencySerializer

class OrderStatementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatementModel
        fields = ('__all__')


