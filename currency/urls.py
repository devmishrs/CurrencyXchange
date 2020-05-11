from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, LoginViewSet, UserWalletViewSet, ForeignCurrencyWalletViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'wallet', UserWalletViewSet)
router.register(r'foreign_currency_wallet', ForeignCurrencyWalletViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'login/', LoginViewSet.as_view(), name='login'),
]
