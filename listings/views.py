from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests

from django.views import generic
from .models import Listing, Review
from .forms import ReviewForm, ListingForm

GEOCODING_API_KEY = 'AIzaSyB_AAHgx8qJADN8uk1N2Qa_qcDLxm21054'

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'listings/index.html'
    context_object_name = 'listing_list'

    def get_queryset(self):
        return Listing.objects.order_by('-rating')


class DetailView(generic.DetailView):
    model = Listing
    template_name = 'listings/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'order' in self.kwargs:
            context['order'] = self.kwargs['order']
        else:
            context['order'] = 'date'
        return context

    def get_queryset(self):
        # no special filtering here
        return Listing.objects.all()


def review(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    form = ReviewForm(request.POST)
    if 'cancel' in request.POST:
        return HttpResponseRedirect(reverse('listings:detail_rev', kwargs={'pk': listing_id}))

    if form.is_valid():
        rev = Review()
        if request.user.username != '':
            rev.user = request.user.username
        rev.listing = listing
        rev.rating = form.cleaned_data['rating']
        rev.review_text = form.cleaned_data['review']
        rev.save()

        reviews = Review.objects.filter(listing_id=listing.id)
        num = 0
        rating = 0
        for review in reviews:
           num += 1
           rating += review.rating 

        setattr(listing, "rating", rating/num)
        listing.save()

        return HttpResponseRedirect(reverse('listings:detail_rev', kwargs={'pk': listing_id}))
    else:
        form = ReviewForm()

    return render(request, 'listings/review.html', {
        'listing': listing,
        'form': form
    })


def listing_view(request):
    form = ListingForm(request.POST)
    if 'cancel' in request.POST:
        return HttpResponseRedirect(reverse('listings:index'))

    if form.is_valid():
        listing = Listing()

        listing.address = form.cleaned_data['address']
        listing.name = form.cleaned_data['name']
        listing.is_house = form.cleaned_data['is_house']
        listing.aircon = form.cleaned_data['aircon']
        listing.furnished = form.cleaned_data['furnished']
        listing.has_pool = form.cleaned_data['has_pool']
        listing.pets_allowed = form.cleaned_data['pets_allowed']
        listing.has_gym = form.cleaned_data['has_gym']
        listing.unit_laundry = form.cleaned_data['unit_laundry']
        listing.shared_laundry = form.cleaned_data['shared_laundry']
        listing.rating = form.cleaned_data['rating']
        listing.rent = form.cleaned_data['rent']
        listing.beds = form.cleaned_data['beds']
        listing.baths = form.cleaned_data['baths']
        listing.desc = form.cleaned_data['desc']
        listing.link = form.cleaned_data['link']

        geo_request = {'key': GEOCODING_API_KEY, 'address': listing.address}
        geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

        geo_resp = requests.get(geocode_url, params=geo_request).json()
        if geo_resp['status'] == 'OK':
            lat = geo_resp['results'][0]['geometry']['location']['lat']
            lon = geo_resp['results'][0]['geometry']['location']['lng']

        listing.lat = lat
        listing.lon = lon

        listing.save()

        return HttpResponseRedirect(reverse('listings:index'))
    else:
        form = ListingForm()

    return render(request, 'listings/addlisting.html', {'form': form})