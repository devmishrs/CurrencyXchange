import sys
from datetime import datetime
from rest_framework import serializers
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from .models import UserProfile, UserWallet

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

class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWallet
        fields = ('__all__')

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

    def update(self, instance, validated_data, *args, **kwargs):
        print("This is instance ... ",instance)
        print("this is validated_data ",validated_data)
        instance.wallet_balance += validated_data.get('wallet_balance', instance.wallet_balance) 
        instance.update_time = datetime.now() 
        instance.save()
        return instance
