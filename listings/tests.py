from django.test import TestCase
from .models import Listing, Review

# Create your tests here.
class ListingModelTests(TestCase):

    # create a Listing
    def test_listing(self):
        address = "123 road street"
        type = "house"
        rent = 800
        l = Listing(address=address, type=type, rent=rent)
        self.assertTrue(l)

class ReviewModelTests(TestCase):

    # create a Review
    def test_review(self):
        address = "123 road street"
        type = "house"
        rent = 800
        l = Listing(address=address, type=type, rent=rent)
        r = Review(listing=l, rating=3, review_text="ok")
        self.assertTrue(r)
    
    # confirm review_num updates properly
    def add_rating(self):
        address = "123 road street"
        type = "house"
        rent = 800
        l = Listing(address=address, type=type, rent=rent)
        Review(listing=l, rating=4, review_text="good")
        self.assertEqual(l.review_num, 1)

    # confirm avg rating updates properly
    def add_rating(self):
        address = "123 road street"
        type = "house"
        rent = 800
        l = Listing(address=address, type=type, rent=rent)
        Review(listing=l, rating=4, review_text="good")
        Review(listing=l, rating=5, review_text="great")
        self.assertEqual(l.rating, 4.5)