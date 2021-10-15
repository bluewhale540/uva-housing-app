from django.urls import include, path
from . import views

app_name = 'login'

urlpatterns = [
    path('logout/', views.account_logout, name='logout')
]
