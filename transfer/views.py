from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from currency.models import UserWallet
from .serializer import OrderStatementModelSerializer 
from .models import OrderStatementModel

# Create your views here.

class Transfer(ModelViewSet):
    queryset = OrderStatementModel.objects.all() 
    serializer_class = OrderStatementModelSerializer
    authentication_class = []

    @action(detail=False, method=['post'])
    def convert_to_foreign_currency(self, request):
        data = request.data
        user = data.get('user',None)
        if user:
            get_wallet = UserWallet.objects.get(user=user)
            get_foreign_wallet = ForeignCurrencyWallet.objects.get(user=user)
            if not get_foreign_wallet:
                return()
        pass
