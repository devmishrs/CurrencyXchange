from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from currency.models import UserWallet, ForeignCurrencyWallet
from .serializers import (OrderStatementModelSerializer, OrderUserWalletSerializer,
                         OrderForeignCurrencyWalletSerializer)
from .models import OrderStatementModel

# Create your views here.

class OneUserTOtherUserWallet(ModelViewSet):
    queryset = UserWallet.objects.all() 
    serializer_class = OrderStatementModelSerializer
    authentication_class = []

    def update(self, request, pk=None):
        data = request.data
        queryset = UserWallet.objects.get(pk=pk)
        serializer = OrderUserWalletSerializer(queryset, data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ConvertToForeignCurrency(ModelViewSet):
    queryset = ForeignCurrencyWallet.objects.all() 
    serializer_class = OrderForeignCurrencyWalletSerializer
    authentication_class = []


    def update(self, request, pk=None):
        data = request.data
        queryset = ForeignCurrencyWallet.objects.get(pk=pk) 
        serializer = OrderForeignCurrencyWalletSerializer(queryset, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
