from django.db import models


# Create your models here.
class Listing(models.Model):
    # long & lat are for gps coords
    # longitude = models.FloatField()
    # latitude = models.FloatField()

    address = models.CharField(max_length=250)
    rating = models.FloatField()  # average of ratings from reviews
    type = models.CharField(max_length=25)  # either house or apt
    rent = models.IntegerField()  # in $

    # dateListed = models.DateTimeField()

    def __str__(self):
        return self.address

    # possible methods: was_listed_recent


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image = models.ImageField()


class Review(models.Model):
    user = models.CharField(max_length=100, default='anonymous')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.IntegerField()  # will need some kind of validation system so input is 1-5
    # ratings maybe should be able to be submitted without a write-up. like just a star rating
    # if we do this, we should then only display reviews with non-empty review_text fields
    # but use all of them for calculating the average rating
    review_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.review_text
