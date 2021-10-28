from django.shortcuts import render

from django.views import generic
from .models import Listing, Review

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'listings/index.html'
    context_object_name = 'listing_list'

    def get_queryset(self):
        return Listing.objects.all()
