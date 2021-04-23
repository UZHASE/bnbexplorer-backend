from unittest import TestCase

from server.repositories.review_repsotory import Review as Review_Repository


class TestReview(TestCase):

    ########################
    #   Test: get_by_id    #
    ########################
    def test_get_by_id_successful(self):
        listing_id = 5121
        reviews = Review_Repository().get_all_by_listing_id(listing_id)

        self.assertTrue(reviews)
        self.assertEqual(50, len(reviews))

    def test_get_by_id_empty(self):
        listing_id = -1
        reviews = Review_Repository().get_all_by_listing_id(listing_id)

        self.assertEqual([], reviews)
        self.assertEqual(0, len(reviews))