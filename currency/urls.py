from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, LoginViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'login/', LoginViewSet.as_view(), name='login'),
]
