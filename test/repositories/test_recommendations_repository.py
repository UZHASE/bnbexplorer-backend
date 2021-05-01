from unittest import TestCase

from server.repositories.recommendations_repository import RecommendationsRepository
from server.models.listings_filter import ListingsFilter


class TestRecommendations(TestCase):

    ########################################
    #   Test: test_recommend_n_listings    #
    ########################################
    def test_recommend_n_listings_successful(self):
        target_id = 2539
        default_num_of_recs = 5
        recommendations = RecommendationsRepository().recommend_n_listings(target_id, ListingsFilter())
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(default_num_of_recs, len(recommendations))

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
        target_id = 2539
        num_of_recs = 1
        # dict size exceeds sampling size
        listing_dict = {
            target_id: [-73.97237, 40.64749, 1, 149, 1, 9, 365],
            1: [-73.97237, 40.04749, 1, 100, 5, 12, 365],
            2: [-80.97237, 50.04749, 2, 1, 55, 999, 1],
            3: [-90.97237, 60.04749, 2, 100, 55, 12, 1],
            4: [-100.97237, 70.04749, 3, 100, 55, 12, 1],
            5: [-90.97237, 80.04749, 3, 100, 55, 12, 1],
            6: [-80.97237, 90.04749, 3, 100, 55, 12, 1],
        }
        recommendations = RecommendationsRepository().compute_n_recommendations(listing_dict, target_id, n=num_of_recs)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(num_of_recs, len(recommendations))
        self.assertEqual(1, len(recommendations))

    def test_compute_n_recommendations_sample_size_smaller_than_n(self):
        target_id = 2539
        num_of_recs = 1
        # dict size is less than sampling size
        listing_dict = {
            target_id: [-73.97237, 40.64749, 1, 149, 1, 9, 365],
            1: [-70.97237, 40.04749, 1, 100, 5, 12, 365],
            2: [-80.97237, 50.04749, 2, 100, 55, 12, 1]
        }
        recommendations = RecommendationsRepository().compute_n_recommendations(listing_dict, target_id, n=num_of_recs)
        # matches a listing with given ID
        self.assertTrue(recommendations)
        self.assertEqual(num_of_recs, len(recommendations))
        self.assertEqual(1, len(recommendations))

    def test_compute_n_recommendations_listing_id_not_found(self):
        target_id = 9   # no match for this ID
        num_of_recs = 1
        # dict size exceeds sampling size
        listing_dict = {
            0: [-73.97237, 40.64749, 1, 149, 1, 9, 365],
            1: [-73.97237, 40.04749, 1, 100, 5, 12, 365],
            2: [-80.97237, 50.04749, 2, 1, 55, 999, 1],
            3: [-90.97237, 60.04749, 2, 100, 55, 12, 1],
            4: [-100.97237, 70.04749, 3, 100, 55, 12, 1],
            5: [-90.97237, 80.04749, 3, 100, 55, 12, 1],
            6: [-80.97237, 90.04749, 3, 100, 55, 12, 1],
        }
        with self.assertRaises(ValueError):
            RecommendationsRepository().compute_n_recommendations(listing_dict, target_id, n=num_of_recs)

    def test_compute_n_recommendations_no_dict_provided(self):
        target_id = 2539
        num_of_recs = 1
        listing_dict = None
        with self.assertRaises(ValueError):
            RecommendationsRepository().compute_n_recommendations(listing_dict, target_id, n=num_of_recs)

    def test_compute_n_recommendations_no_target_id_provided(self):
        target_id = None
        num_of_recs = 1
        # dict size is less than sampling size
        listing_dict = {
            target_id: [-73.97237, 40.64749, 1, 149, 1, 9, 365],
            1: [-70.97237, 40.04749, 1, 100, 5, 12, 365],
            2: [-80.97237, 50.04749, 2, 100, 55, 12, 1]
        }
        with self.assertRaises(ValueError):
            RecommendationsRepository().compute_n_recommendations(listing_dict, target_id, n=num_of_recs)

    ########################################
    #   Test: euclidean_distance    #
    ########################################
    def test_euclidean_distance_successful(self):
        row = [3, 3, 3, 3, 3, 3, 3]
        target = [1, 1, 1, 1, 1, 1, 1]
        distance = RecommendationsRepository().euclidean_distance(target, row)
        # compute distance
        self.assertEqual(5.291502622129181, distance)

    def test_euclidean_distance_empty_arrays(self):
        row = []
        target = []
        distance = RecommendationsRepository().euclidean_distance(target, row)
        # compute distance
        self.assertEqual(0, distance)

    def test_euclidean_distance_no_args_provided(self):
        row = None
        target = None
        # compute distance
        with self.assertRaises(ValueError):
            RecommendationsRepository().euclidean_distance(target, row)

    ##########################
    #   Test: map_result    #
    ##########################
    def test_map_result_successful(self):
        row = [[-73.97237, 40.64749, 1, 149, 1, 9, 365]]
        expected_dict = {-73.97237: [40.64749, 1, 149, 1, 9, 365]}
        actual_dict = RecommendationsRepository().map_result(row)
        self.assertEqual(expected_dict, actual_dict)