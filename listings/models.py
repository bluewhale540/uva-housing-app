from django.db import models
from django.utils import timezone


# Create your models here.
class Listing(models.Model):
    # long & lat are for gps coords
    # longitude = models.FloatField()
    # latitude = models.FloatField()

    address = models.CharField(max_length=250)
    name = models.CharField(max_length=100, default='NO_NAME')
    is_house = models.BooleanField()  # 0 = apt, 1 = house

    # amenities
    aircon = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)
    has_gym = models.BooleanField(default=False)
    unit_laundry = models.BooleanField(default=False)
    shared_laundry = models.BooleanField(default=False)

    rating = models.FloatField()  # average of ratings from reviews

    rent = models.IntegerField()  # in $
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    desc = models.TextField(default='NO_DESCRIPTION')  # description of listing
    link = models.URLField(max_length=100, default='NO_LINK')

    lat = models.DecimalField(default=0, decimal_places=7, max_digits=10)
    lon = models.DecimalField(default=0, decimal_places=7, max_digits=10)

    # dateListed = models.DateTimeField()

    def __str__(self):
        return self.name

    # possible methods: was_listed_recent


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Review(models.Model):
    user = models.CharField(max_length=100, default='anonymous')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date = models.DateTimeField('date posted', default=timezone.now)
    rating = models.IntegerField()  # will need some kind of validation system so input is 1-5
    # ratings maybe should be able to be submitted without a write-up. like just a star rating
    # if we do this, we should then only display reviews with non-empty review_text fields
    # but use all of them for calculating the average rating
    review_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.review_text
