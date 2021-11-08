from django.urls import include, path

from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>', views.DetailView.as_view(), name='detail_rev'),
    path('<int:pk>/<str:order>', views.DetailView.as_view(), name='detail'),
    path('<int:listing_id>/review/', views.review, name='review'),
]
