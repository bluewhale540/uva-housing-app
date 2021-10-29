from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Listing, Review
from .forms import ReviewForm


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'listings/index.html'
    context_object_name = 'listing_list'

    def get_queryset(self):
        return Listing.objects.all()


class DetailView(generic.DetailView):
    model = Listing
    template_name = 'listings/detail.html'

    def get_queryset(self):
        # no special filtering here
        return Listing.objects.all()


def review(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    form = ReviewForm(request.POST)
    return render(request, 'listings/review.html', {
        'listing': listing,
        'form': form
    })
