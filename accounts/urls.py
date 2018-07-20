from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('api/users/', views.UserCreate.as_view(), name='account-create'),
    path('login', views.login),
]