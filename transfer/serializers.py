import sys
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import OrderStatementModel 
from CurrencyXchange import constants
from currency.utils.pdf_conv import text_to_pdf
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
        try:
            print("This is updatei",validated_data)
            method = validated_data.get('method')
            amount = validated_data.get('wallet_balance')
            if str(method) == constants.PAY_METHOD[0][1]:
                ## CREDIT method
                print(amount,"Inside of method")
                print(type(amount), type(instance.wallet_balance))
                user = validated_data.get('user')
                instance.wallet_balance += amount
                wallet = UserWallet.objects.get(user=user)
                wallet.wallet_balance -= amount
                or_obj = OrderStatementModel.objects.create(to_self=False,method=method, transaction_amount=amount, \
                            from_wallet=instance, to_wallet=wallet, is_success=True, is_foreingn=False)
                wallet.save()
                # text_to_pdf(name=wallet.user.username, method=method, amount=amount)  # To generate PDF
                instance.save()
            elif str(method) == constants.PAY_METHOD[1][1]:
                ## DEBIT method
                user = validated_data.get('user')
                wallet = UserWallet.objects.get(user=user)
                print(amount,"Inside of method",wallet.wallet_balance)
                if wallet.wallet_balance > amount:
                    print(amount,"Inside of method",wallet.wallet_balance)
                    instance.wallet_balance -= amount
                    wallet = UserWallet.objects.get(user=user)
                    wallet.wallet_balance += amount
                    wallet.save()
                    or_obj = OrderStatementModel.objects.create(to_self=True, method=method, transaction_amount=amount, \
                            from_wallet=wallet,to_wallet=instance, is_success=True, is_foreingn=False)
                    # text_to_pdf(name=wallet.user.username, method=method, amount=amount)  # To generate PDF
                    instance.save()
                else:
                    raise serializers.ValidationError('Insufficient balance')
            return instance
        except Exception as e:
            print("Line at {}".format(sys.exc_info()[-1].tb_lineno))
            print("This is Exception :", e)

class OrderForeignCurrencyWalletSerializer(serializers.ModelSerializer):
    """ Before use this method Make sure Foreign currency wallet must be created.. Otherwise you will get error"""
    class Meta:
        model = ForeignCurrencyWallet
        fields = ('__all__')


    def update(self, instance, validated_data, *args, **kwargs):
        try:
            print("Foreign validated data",validated_data)
            print("This is instance..",instance)
            amount = validated_data.get('balance')
            currency = validated_data.get('currency')
            currency_value = get_currency_converted_balance('INR',str(currency),amount) 
            wallet = UserWallet.objects.get(user=instance.user)
            wallet.wallet_balance -= currency_value 
            wallet.save()
            instance.balance = currency_value
            instance.save()
            or_obj = OrderStatementModel.objects.create(to_self=False, method_id=2, transaction_amount=amount, \
                            from_wallet=wallet,to_foreign_wallet=instance, is_success=True, is_foreingn=True)

            return instance
        except Exception as e:
            print('Here Error is >> ',e)
            print("Line at {}".format(sys.exc_info()[-1].tb_lineno))
