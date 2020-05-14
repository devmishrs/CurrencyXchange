from django.conf.urls import url, include
from rest_framework import routers
from .views import (OneUserTOtherUserWallet,ConvertToForeignCurrency)

router = routers.DefaultRouter()
router.register(r'convert_to_foreign_currency', ConvertToForeignCurrency)
router.register(r'one_user_to_other_user_wallet', OneUserTOtherUserWallet)

urlpatterns = [
    url(r'', include(router.urls)),
]
