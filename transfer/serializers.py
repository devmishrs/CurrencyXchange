from rest_framework import serializers
from .models import OrderStatementModel 
from CurrencyXchange import constants
from currency.models import UserWallet, ForeignCurrencyWallet
from currency.serializers import UserWalletSerializer
from currency.utils.views import get_currency_converted_balance

class OrderStatementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatementModel
        fields = ('__all__')

class OrderUserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWallet
        fields = ('__all__')

    def update(self, instance, validated_data, *args, **kwargs):
        print("This is updatei",validated_data)
        method = validated_data.get('method')
        amount = validated_data.get('transaction_amount')
        if method == constants.PAY_METHOD[0][1]:
            ## CREDIT method
            user = validated_data.get('user')
            instance.wallet_balance += amount
            wallet = UserWallet.objects.get(user=user)
            wallet.wallet_balance -= amount
            wallet.save()
            insatnce.save()
        elif method == constants.PAY_METHOD[1][1]:
            ## DEBIT method
            user = validated_data.get('user')
            wallet = UserWallet.objects.get(user=user)
            if wallet.wallet_balance > amount:
                insatnce.wallet_balance -= amount
                wallet = User.objects.get(user=user)
                wallet.wallet_balance += amount
                wallet.save()
                insatnce.save()
        return instance



class OrderForeignCurrencyWalletSerializer(serializers.ModelSerializer):
    """ Before use this method Make sure Foreign currency wallet must be created.. Otherwise you will get error"""
    class Meta:
        model = ForeignCurrencyWallet
        fields = ('__all__')

    def update(self, instance, validated_data, *args, **kwargs):
        print("Foreign validated data",validated_data)
        print("This is instance..",instance)
        amount = validated_data.get('balance')
        currency = validated_data.get('currency')
        currency_value = get_currency_converted_balance('INR',str(currency),amount) 
        wallet = User.objects.get(user=instance.user)
        wallet.wallet_balance -= currency_value 
        wallet.save()
        instance.balance = currency_value
        instance.save()
        return instance
