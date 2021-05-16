from unittest import TestCase

from server.repositories.recommendations_repository import RecommendationsRepository
from server.models.listings_filter import ListingsFilter
from server.models.listing import Listing


class TestRecommendations(TestCase):

    ########################################
    #   Test: test_recommend_n_listings    #
    ########################################
    def test_recommend_n_listings_successful_with_empty_filter(self):
        target_id = 2539
        default_num_of_recs = 5
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, ListingsFilter())
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_full_filter(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None, # to not be too restrictive, we need a result set and not an exact match
            host_id=None,  # to not be too restrictive, we need a result set and not an exact match
            host_name="John",
            neighbourhood=["Brooklyn"],
            area=None, # to not be too restrictive, we need a result set and not an exact match
            price_min=50,
            price_max=500,
            min_nights=1,
            availability=1,
            listings_per_host=1,
            room_type=None  # to not be too restrictive, we need a result set and not an exact match
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_listing_name(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name="a",
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None  # to not be too restrictive, we need a result set and not an exact match
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_host_id(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=190921808,  # expected to have many listings for this host
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_host_name(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name="John",  # expected to have many listings for this host
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_neighbourhood(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=['Brooklyn'],
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_area(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=['Flatlands'],
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_price_min(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=1,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_price_max(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=200,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_availability(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=100,
            listings_per_host=None,
            room_type=None
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_listings_per_host(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=1,
            room_type=None
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_successful_with_room_type(self):
        target_id = 2539
        default_num_of_recs = 5
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=['Entire home/apt']
        )
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, given_filter)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

    def test_recommend_n_listings_unsuccessful_filters_too_restrictive(self):
        target_id = 2539
        expected_result = []
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name='John',
            neighbourhood=None,
            area=None,
            price_min=500,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=['Entire home/apt']
        )
        # filters are too restrictive!
        self.assertEqual(expected_result, RecommendationsRepository().recommend_n_listings(target_id, given_filter))

    def test_recommend_n_listings_successful_return_1_recommendation(self):
        target_id = 2539
        n = 1
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, ListingsFilter(), n=n)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(n, len(recommendations))

    def test_recommend_n_listings_no_filter_provided(self):
        target_id = 2539
        # no filter is provided -> Exception
        with self.assertRaises(ValueError):
            RecommendationsRepository().recommend_n_listings(target_id, None)

    def test_recommend_n_listings_no_id_provided(self):
        target_id = None
        # no ID is provided -> Exception
        with self.assertRaises(ValueError):
            RecommendationsRepository().recommend_n_listings(target_id, ListingsFilter())

    def test_recommend_n_listings_no_match_for_id(self):
        # no match for this ID
        target_id = 1
        with self.assertRaises(ValueError):
            RecommendationsRepository().recommend_n_listings(target_id, ListingsFilter())

    def test_recommend_n_listings_n_too_small(self):
        target_id = 2539
        # n is too small
        n = 0
        with self.assertRaises(ValueError):
            RecommendationsRepository().recommend_n_listings(target_id, ListingsFilter(), n=n)

    ########################################
    #   Test: compute_n_recommendations    #
    ########################################
    def test_compute_n_recommendations_successful(self):
        target = Listing(2539, "listing", None, None, None, -73.97237, 40.64749, 'Single Room', 149, 1, 9, 365)
        num_of_recs = 1
        # dict size exceeds sampling size
        listing_dict = {
            1: [-73.97237, 40.04749, 1, 100, 5, 12, 365],
            2: [-80.97237, 50.04749, 2, 1, 55, 999, 1],
            3: [-90.97237, 60.04749, 2, 100, 55, 12, 1],
            4: [-100.97237, 70.04749, 3, 100, 55, 12, 1],
            5: [-90.97237, 80.04749, 3, 100, 55, 12, 1],
            6: [-80.97237, 90.04749, 3, 100, 55, 12, 1],
        }
        recommendations = RecommendationsRepository()._compute_n_recommendations(listing_dict, target, n=num_of_recs)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(num_of_recs, len(recommendations))

    def test_compute_n_recommendations_successful_target_contained_in_dict(self):
        target = Listing(1, "listing", None, None, None, -73.97237, 40.64749, 'Single Room', 149, 1, 9, 365)
        num_of_recs = 1
        # dict size exceeds sampling size
        listing_dict = {
            1: [-73.97237, 40.04749, 1, 100, 5, 12, 365],
            2: [-80.97237, 50.04749, 2, 1, 55, 999, 1],
            3: [-90.97237, 60.04749, 2, 100, 55, 12, 1],
            4: [-100.97237, 70.04749, 3, 100, 55, 12, 1],
            5: [-90.97237, 80.04749, 3, 100, 55, 12, 1],
            6: [-80.97237, 90.04749, 3, 100, 55, 12, 1],
        }
        recommendations = RecommendationsRepository()._compute_n_recommendations(listing_dict, target, n=num_of_recs)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(num_of_recs, len(recommendations))

    def test_compute_n_recommendations_sample_size_smaller_than_n(self):
        target = Listing(2539, "listing", None, None, None, -73.97237, 40.64749, 'Single Room', 149, 1, 9, 365)
        num_of_recs = 1
        # dict size is less than sampling size
        listing_dict = {
            target.id: [-73.97237, 40.64749, 1, 149, 1, 9, 365],
            1: [-70.97237, 40.04749, 1, 100, 5, 12, 365],
            2: [-80.97237, 50.04749, 2, 100, 55, 12, 1]
        }
        recommendations = RecommendationsRepository()._compute_n_recommendations(listing_dict, target, n=num_of_recs)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(num_of_recs, len(recommendations))

    def test_compute_n_recommendations_no_dict_provided(self):
        target = Listing(2539, "listing", None, None, None, -73.97237, 40.64749, 'Single Room', 149, 1, 9, 365)
        num_of_recs = 1
        listing_dict = None
        with self.assertRaises(ValueError):
            RecommendationsRepository()._compute_n_recommendations(listing_dict, target, n=num_of_recs)

    def test_compute_n_recommendations_no_target_id_provided(self):
        target = None
        num_of_recs = 1
        # dict size is less than sampling size
        listing_dict = {
            1: [-73.97237, 40.64749, 1, 149, 1, 9, 365],
            2: [-70.97237, 40.04749, 1, 100, 5, 12, 365],
            3: [-80.97237, 50.04749, 2, 100, 55, 12, 1]
        }
        with self.assertRaises(ValueError):
            RecommendationsRepository()._compute_n_recommendations(listing_dict, target, n=num_of_recs)

    ########################################
    #   Test: euclidean_distance    #
    ########################################
    def test_euclidean_distance_successful(self):
        row = [3, 3, 3, 3, 3, 3, 3]
        target = [1, 1, 1, 1, 1, 1, 1]
        distance = RecommendationsRepository()._euclidean_distance(target, row)
        # compute distance
        self.assertEqual(5.291502622129181, distance)

    def test_euclidean_distance_empty_arrays(self):
        row = []
        target = []
        distance = RecommendationsRepository()._euclidean_distance(target, row)
        # compute distance
        self.assertEqual(0, distance)

    def test_euclidean_distance_no_args_provided(self):
        row = None
        target = None
        # compute distance
        with self.assertRaises(ValueError):
            RecommendationsRepository()._euclidean_distance(target, row)

    ##########################
    #   Test: map_result    #
    ##########################
    def test_map_result_successful(self):
        row = [[-73.97237, 40.64749, 1, 149, 1, 9, 365]]
        expected_dict = {-73.97237: [40.64749, 1, 149, 1, 9, 365]}
        actual_dict = RecommendationsRepository()._map_result(row)
        self.assertEqual(expected_dict, actual_dict)