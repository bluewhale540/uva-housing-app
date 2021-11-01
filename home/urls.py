from django.urls import include, path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.home, name='home'),
]
