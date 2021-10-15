from django.urls import include, path

from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'login'

urlpatterns = [
    path('logout/', views.account_logout, name='logout')
]
