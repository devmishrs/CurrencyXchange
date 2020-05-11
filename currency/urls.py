from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, LoginViewSet, UserWalletViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'wallet', UserWalletViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'login/', LoginViewSet.as_view(), name='login'),
]
