from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile, Currencies, UserWallet
from .serializers import (UserSerializer, LoginSerializer,
                          UserWalletSerializer, UserWalletViewSerializer)

# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated,]
    authentication_classes = []


class LoginViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        data = request.POST

        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
           user = serializer.validated_data['user'] 
           login(request, user)
           print('Login success')
           return Response(status=status.HTTP_201_CREATED, data={'user_id':user.id})
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, error=serializer.errors)
       

class UserWalletViewSet(ModelViewSet):
    queryset = UserWallet.objects.all()
    serializer_class = [UserWalletSerializer,]
    #permission_classes = [IsAuthenticated,]
    authentication_classes = []

    def retrieve(self, request, pk=None):
        try:
            print('Called retrive..')
            queryset = UserWallet.objects.get(pk=pk)
            serializer = UserWalletViewSerializer(queryset)
            return Response(serializer.data)
        except Exception as e:
            print("Error in >>> ",e)

    def update(self, request, pk=None):
        print(request.data)
        print("Called update")
        data = request.data
        queryset = UserWallet.objects.get(pk=pk)
        serializer = UserWalletSerializer(queryset, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
