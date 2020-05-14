from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from currency.models import UserWallet, ForeignCurrencyWallet
from currency.utils.pdf_conv import text_to_pdf
from .serializers import (OrderStatementModelSerializer, OrderUserWalletSerializer,
                         OrderForeignCurrencyWalletSerializer)
from .models import OrderStatementModel

# Create your views here.

class OneUserTOtherUserWallet(ModelViewSet):
    queryset = UserWallet.objects.all() 
    serializer_class = OrderUserWalletSerializer
    authentication_classes = []

    def retrieve(self, request, pk=None):
        print("This is Retrieve : ",pk)
        queryset = UserWallet.objects.get(user=pk)
        print("This is queryset  ",queryset)
        serializer = OrderUserWalletSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        data = request.data
        print("Data :: ",request.data)
        queryset = UserWallet.objects.get(user=pk)
        serializer = OrderUserWalletSerializer(queryset, data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ConvertToForeignCurrency(ModelViewSet):
    queryset = ForeignCurrencyWallet.objects.all() 
    serializer_class = OrderForeignCurrencyWalletSerializer
    authentication_classes = []


    def retrieve(self, request, pk=None):
        print("This is retrieve :: ",pk)
        queryset = ForeignCurrencyWallet.objects.get(user_id=pk)
        serializer = OrderForeignCurrencyWalletSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        print("This is PK ",pk)
        data = request.data
        queryset = ForeignCurrencyWallet.objects.get(user_id=pk) 
        serializer = OrderForeignCurrencyWalletSerializer(queryset, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


