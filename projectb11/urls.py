from django.urls import path

from . import views

app_name = 'projectb11'

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.home, name='home')
]
