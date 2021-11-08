from django.test import TestCase
from .models import Listing, Review


# Create your tests here.
class ListingModelTests(TestCase):

    # create a Listing
    def test_listing(self):
        address = "123 road street"
        is_house = True
        rent = 800
        l = Listing(address=address, is_house=is_house, rent=rent)
        self.assertTrue(l)


class ReviewModelTests(TestCase):

    # create a Review
    def test_review(self):
        address = "123 road street"
        is_house = True
        rent = 800
        l = Listing(address=address, is_house=is_house, rent=rent)
        r = Review(listing=l, rating=3, review_text="ok")
        self.assertTrue(r)

    # confirm review_num updates properly
    def add_rating(self):
        address = "123 road street"
        is_house = True
        rent = 800
        l = Listing(address=address, is_house=is_house, rent=rent)
        Review(listing=l, rating=4, review_text="good")
        Review(listing=l, rating=5, review_text="great")
        self.assertEqual(l.review_num, 2)
        self.assertEqual(l.rating, 4.5)
