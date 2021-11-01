from django.contrib import admin
from .models import Listing, Review, ListingImage


# Register your models here.
class ImageInLine(admin.TabularInline):
    model = ListingImage
    extra = 1


class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1


class ListingAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, ReviewInLine]


admin.site.register(Listing, ListingAdmin)
