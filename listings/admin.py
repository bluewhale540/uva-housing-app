from django.contrib import admin
from .models import Listing, Review


# Register your models here.
class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 3


class ListingAdmin(admin.ModelAdmin):
    inlines = [ReviewInLine]


admin.site.register(Listing, ListingAdmin)
