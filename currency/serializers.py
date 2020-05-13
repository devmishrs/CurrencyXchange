import sys
from datetime import datetime
from rest_framework import serializers
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from .models import UserProfile, UserWallet, Currencies, ForeignCurrencyWallet
from .utils.views import get_currency_converted_balance

class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = ('__all__')
class UserStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email'
        )

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('__all__')
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def update(self, instance, validated_data, *args, **kwargs):
        print("This is validated_data :",validated_data)
        instance.address = validated_data.get('address', instance.address)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.save()
        return instance
        

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=22)
    password = serializers.CharField(max_length=55, style={'input_type':'password'})
    class Meta:
        model = User
        fields = ('__all__')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        try:
            if username and password:
                user = User.objects.get(username=username)
                if user:
                    if user.is_active:
                        user = authenticate(username=username, password=password)
                        data['user'] = user
                        return data
                    else:
                        raise serializers.ValidationError('User is no longer active.')
                else:
                    raise ValidationError('User does not exists.')
            else:
                raise serializers.ValidationError('Credentials are required to login.')
        except Exception as e:
            print('Found Exception in user login.. ',e)
            print('Line no : ',sys.exc_info()[-1].tb_lineno)

class UserWalletViewSerializer(serializers.ModelSerializer):
    currency_type = serializers.StringRelatedField()
    update_time = serializers.DateTimeField(format="%d %b-%Y: %H:%M:%S")
    user = serializers.StringRelatedField() 

    class Meta:
        model = UserWallet
        fields = ('__all__')

class UserWalletSerializer(serializers.ModelSerializer):
    #currency_type = CurrenciesSerializer()
    class Meta:
        model = UserWallet
        fields = ('__all__')

   
    def update(self, instance, validated_data, *args, **kwargs):
        print("This is instance ... ",instance)
        print("this is validated_data ",validated_data)
        instance.wallet_balance += validated_data.get('wallet_balance', instance.wallet_balance) 
        if 'currency_type' in validated_data:
            prev_currency = instance.currency_type
            new_currency = validated_data.get('currency_type', instance.currency_type)
            instance.currency_type = new_currency
            current_bal = get_currency_converted_balance(str(prev_currency), str(new_currency), instance.wallet_balance)
            instance.wallet_balance = current_bal
        instance.update_time = datetime.now() 
        instance.save()
        return instance

class ForeignCurrencyWalletViewSerializer(serializers.ModelSerializer):
    currency = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    update_time = serializers.DateTimeField(format="%d %b-%Y: %H:%M:%S")
    class Meta:
        model = ForeignCurrencyWallet
        fields = ('__all__')

class ForeignCurrencyWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignCurrencyWallet
        fields = ('__all__')

    def create(self, validated_data):
        print("This is validated data ",validated_data)
        user = validated_data.get('user')
        currency = validated_data.get('currency')
        balance = validated_data.get('balance')
        wallet, is_created = ForeignCurrencyWallet.objects.get_or_create(user=user)
        if is_created:
            wallet.currency = currency
            wallet.balance = balance
        else:
            wallet.balance += balance
        wallet.save()
        return wallet

    #def create(self, data):
    #    print("Validated data: ",validated_data)
    #    amount = validated_data.get('amount')
    #    user = validated_data.get('user')
    #    user = User.objects.get(id=user)
    #    user_wallet, is_created = UserWallet.objects.get_or_create(user=user)
    #    if is_created:
    #        user_wallet.wallet_balance = amount
    #    else:
    #        user_wallet.wallet_balance += amount
    #    user_wallet.save()
    #    return user_wallet
