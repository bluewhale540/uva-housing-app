from django.urls import include, path

from . import views

app_name = 'listings'
urlpatterns = [
    # /listings
    path('', views.IndexView.as_view(), name="index"),
    # /listings/1
    path('<int:pk>', views.DetailView.as_view(), name='detail_rev'),
    # /listings/1/date
    path('<int:pk>/<str:order>', views.DetailView.as_view(), name='detail'),
    path('<int:listing_id>/review/', views.review, name='review'),
    path('addlisting/', views.listing_view, name='add')
]
