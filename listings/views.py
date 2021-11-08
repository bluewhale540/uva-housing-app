from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views import generic
from .models import Listing, Review
from .forms import ReviewForm, ListingForm


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

        setattr(listing, "rating", (listing.rating * listing.review_num + int(rev.rating)) / (listing.review_num + 1))
        setattr(listing, "review_num", listing.review_num + 1)
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
        listing.rating = form.cleaned_data['rating']
        listing.review_num = form.cleaned_data['review_num']
        listing.rent = form.cleaned_data['rent']
        listing.beds = form.cleaned_data['beds']
        listing.baths = form.cleaned_data['baths']
        listing.desc = form.cleaned_data['desc']
        listing.link = form.cleaned_data['link']
        listing.save()

        return HttpResponseRedirect(reverse('listings:index'))
    else:
        form = ListingForm()

    return render(request, 'listings/addlisting.html', {'form': form})