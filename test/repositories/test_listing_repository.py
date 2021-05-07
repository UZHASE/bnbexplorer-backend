import re
from unittest import TestCase

from server.models.listings_filter import ListingsFilter
from server.repositories.listing_repsotory import Listing


class TestListing(TestCase):

    ########################
    #   Test: get_by_id    #
    ########################
    def test_get_by_id_successful(self):
        given_id = 2539
        listing = Listing().get_by_id(given_id)
        # matches a listing with given ID
        self.assertTrue(listing)
        self.assertEqual(given_id, listing.id)

    def test_get_by_id_not_found(self):
        # expected no result for this ID
        given_id = 1
        listing = Listing().get_by_id(given_id)
        # no match: Listing is not present
        self.assertFalse(listing)

    ########################
    #   Test: get_all_by_id    #
    ########################
    def test_get_all_by_id_successful(self):
        id_list = [1, 2539]
        listings = Listing().get_all_by_id(id_list)
        # only 1 match!
        self.assertTrue(listings)
        self.assertEqual(1, len(listings))

    def test_get_all_by_id_not_found(self):
        # expected no result for this ID
        id_list = [1]
        listings = Listing().get_all_by_id(id_list)
        # no match: Listing is not present
        self.assertFalse(listings)

    ######################
    #   Test: get_all    #
    ######################
    def test_get_all_with_empty_filter(self):
        # no filter params = retrieve all Listings
        given_filter = ListingsFilter()
        listings = Listing().get_all(given_filter)
        # matches row limit according to base repo
        self.assertEqual(1000, len(listings))

    def test_get_all_with_filter_default_str_values(self):
        # no filter params = retrieve all Listings
        given_filter = ListingsFilter(
            listing_name="",
            host_id=None,
            host_name="",
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # entering blank strings is equal to entering no input: returns 1000 because of LIMIT clause
        self.assertEqual(1000, len(listings))

    def test_get_all_with_filter_array_params_empty(self):
        # no filter params = retrieve all Listings
        given_filter = ListingsFilter(
            listing_name="",
            host_id=None,
            host_name="",
            neighbourhood=[],
            area=[],
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=[]
        )
        listings = Listing().get_all(given_filter)
        # entering blank strings is equal to entering no input: returns 1000 because of LIMIT clause
        self.assertEqual(1000, len(listings))

    def test_get_all_with_filter_array_params_no_matches(self):
        # no filter params = retrieve all Listings
        given_filter = ListingsFilter(
            listing_name="",
            host_id=None,
            host_name="",
            neighbourhood=["no match for this value"],
            area=["no match for this value"],
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=["no match for this value"]
        )
        listings = Listing().get_all(given_filter)
        # entering blank strings is equal to entering no input: returns 1000 because of LIMIT clause
        self.assertEqual(0, len(listings))

    def test_get_all_with_filter_blank_str_values(self):
        # filter params
        given_filter = ListingsFilter(
            listing_name=" ",
            host_id=None,
            host_name=" ",
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # no matches
        self.assertEqual(0, len(listings))

    def test_get_all_with_filter_all_parameters_set(self):
        # all filter params are given
        given_filter = ListingsFilter(
            listing_name="Park Slope Apartment ",
            host_id=4330726,
            host_name="Jon",
            neighbourhood=["Brooklyn"],
            area=["Park Slope"],
            price_min=155,
            price_max=155,
            min_nights=5,
            availability=189,
            listings_per_host=1,
            room_type=["Entire home/apt"]
        )
        listings = Listing().get_all(given_filter)
        # exact match
        self.assertEqual(1, len(listings))

    ############################
    #   'listing_name' tests   #
    ############################
    def test_get_all_with_filter_exact_match_by_listing_name(self):
        # filter by 'listing_name'
        given_filter = ListingsFilter(
            listing_name='Skylit Bedroom In Brooklyn',
            host_id=None,
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
        listings = Listing().get_all(given_filter)
        # exact match
        self.assertEqual(1, len(listings))

    def test_get_all_with_filter_several_matches_by_listing_name(self):
        # filter by 'listing_name'
        given_filter = ListingsFilter(
            listing_name='Sky',
            host_id=None,
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
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(8, len(listings))

    def test_get_all_with_filter_no_match_by_listing_name(self):
        # filter by 'listing_name'
        given_filter = ListingsFilter(
            listing_name='No Match For This Name',
            host_id=None,
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
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(0, len(listings))

    #######################
    #   'host_id' tests   #
    #######################
    def test_get_all_with_filter_exact_matches_by_host_id(self):
        # filter by 'host_id'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=3734323,
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
        listings = Listing().get_all(given_filter)
        # exact matches
        self.assertEqual(2, len(listings))

    def test_get_all_with_filter_by_host_id_negative_number(self):
        # filter by 'host_id'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=-3734323,
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
        listings = Listing().get_all(given_filter)
        # no matches
        self.assertEqual(0, len(listings))

    def test_get_all_with_filter_no_match_by_host_id(self):
        # filter by 'host_id'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=1,
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
        listings = Listing().get_all(given_filter)
        # no matches
        self.assertEqual(0, len(listings))

    #########################
    #   'host_name' tests   #
    #########################
    def test_get_all_with_filter_exact_match_by_host_name(self):
        # filter by 'host_name'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name='Shon',
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # exact match
        self.assertEqual(1, len(listings))

    def test_get_all_with_filter_several_matches_by_host_name(self):
        # filter by 'host_name'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name='Colin',
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(5, len(listings))

    def test_get_all_with_filter_no_match_by_host_name(self):
        # filter by 'host_name'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name='No Match For This Name',
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # no matches
        self.assertEqual(0, len(listings))

    #####################################
    #   'neighbourhood'/ 'area' tests   #
    #####################################
    def test_get_all_with_filter_several_matches_by_neighbourhood_and_area(self):
        # filter by 'neighbourhood'  and 'area'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=['Brooklyn'],
            area=['Kensington'],
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(35, len(listings))

    def test_get_all_with_filter_several_matches_by_neighbourhood_and_area_multiple_input(self):
        # filter by 'neighbourhood'  and 'area'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=['Brooklyn', 'Manhattan'],
            area=['Kensington', 'Inwood'],
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(80, len(listings))

    def test_get_all_with_filter_no_match_by_neighbourhood_and_area(self):
        # filter by 'neighbourhood' and 'area'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=['Brooklyn'],
            area=['Inwood'],
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # no match
        self.assertEqual(0, len(listings))

    ######################################
    #   'price_min'/ 'price_max' tests   #
    ######################################
    def test_get_all_with_filter_match_by_price_min_price_max_0(self):
        # filter by 'price_min' and 'price_max'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=0,
            price_max=0,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # two listings have price = 0
        self.assertEqual(2, len(listings))

    def test_get_all_with_filter_match_by_price_min_price_max_negative(self):
        # filter by 'price_min' and 'price_max'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=-10000,
            price_max=0,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # two listings have price = 0
        self.assertEqual(2, len(listings))

    def test_get_all_with_filter_match_by_price_min_price_max_invalid_range(self):
        # filter by 'price_min' and 'price_max'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=100,
            price_max=50,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # no match as price_min > price_max
        self.assertEqual(0, len(listings))

    def test_get_all_with_filter_several_matches_by_price_min_price_max(self):
        # filter by 'price_min' and 'price_max'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=50,
            price_max=100,
            min_nights=None,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(1000, len(listings))

    ##########################
    #   'min_nights' tests   #
    ##########################
    def test_get_all_with_filter_by_min_nights(self):
        # filter by 'min_nights'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=100,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(24, len(listings))

    def test_get_all_with_filter_by_min_nights_negative_number(self):
        # filter by 'min_nights'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=-10,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # no matches
        self.assertEqual(1000, len(listings))

    def test_get_all_with_filter_no_match_by_min_nights(self):
        # filter by 'min_nights'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=10000,
            availability=None,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # no matches
        self.assertEqual(0, len(listings))

    ############################
    #   'availability' tests   #
    ############################
    def test_get_all_with_filter_by_availability(self):
        # filter by 'availability'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=365,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(203, len(listings))

    def test_get_all_with_filter_by_availability_negative_number(self):
        # filter by 'availability'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=-365,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(1000, len(listings))

    def test_get_all_with_filter_no_match_by_availability(self):
        # filter by 'availability'
        given_filter = ListingsFilter(
            listing_name=None,
            host_id=None,
            host_name=None,
            neighbourhood=None,
            area=None,
            price_min=None,
            price_max=None,
            min_nights=None,
            availability=500,
            listings_per_host=None,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # no matches
        self.assertEqual(0, len(listings))

    #################################
    #   'listings_per_host' tests   #
    #################################
    def test_get_all_with_filter_by_listings_per_host(self):
        # filter by 'listings_per_host'
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
            listings_per_host=200,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(57, len(listings))

    def test_get_all_with_filter_by_listings_per_host_negative_number(self):
        # filter by 'listings_per_host'
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
            listings_per_host=-10,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(1000, len(listings))

    def test_get_all_with_filter_no_match_by_listings_per_host(self):
        # filter by 'listings_per_host'
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
            listings_per_host=1000,
            room_type=None
        )
        listings = Listing().get_all(given_filter)
        # no matches
        self.assertEqual(0, len(listings))

    #########################
    #   'room_type' tests   #
    #########################
    def test_get_all_with_filter_match_by_room_type(self):
        # filter by 'room_type'
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
            room_type=["Private Room"]
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(1000, len(listings))

    def test_get_all_with_filter_match_by_multiple_room_types(self):
        # filter by 'room_type'
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
            room_type=["Private Room", "Entire home/apt"]
        )
        listings = Listing().get_all(given_filter)
        # several matches
        self.assertEqual(1000, len(listings))

    def test_get_all_with_filter_no_match_by_room_type(self):
        # filter by 'room_type'
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
            room_type=['Room']
        )
        listings = Listing().get_all(given_filter)
        # no matches
        self.assertEqual(0, len(listings))

    ###################################
    #   'build_get_all_query' tests   #
    ###################################
    def test_build_get_all_query_with_full_filter(self):
        # build_get_all_query with all filter options
        given_filter = ListingsFilter(
            listing_name="Park Slope Apartment ",
            host_id=4330726,
            host_name="Jon",
            neighbourhood=["Brooklyn"],
            area=["Park Slope"],
            price_min=155,
            price_max=155,
            min_nights=5,
            availability=189,
            listings_per_host=1,
            room_type=["Entire home/apt"]
        )
        expected_query = '''SELECT "listings"."id","listings"."name","listings"."neighbourhood","listings"."area","listings"."longitude","listings"."latitude","listings"."room_type" "roomType","listings"."price","listings"."min_nights" "minNights","listings"."num_of_reviews" "numOfReviews","listings"."availability","hosts"."id" "host_id","hosts"."name" "host_name","hosts"."num_of_listings" FROM "listings" JOIN "hosts" ON "listings"."host_id"="hosts"."id" WHERE LOWER("listings"."name") LIKE LOWER('Park Slope Apartment %') AND "hosts"."id"=4330726 AND LOWER("hosts"."name") LIKE LOWER('Jon%') AND LOWER("listings"."neighbourhood") IN ('brooklyn') AND LOWER("listings"."area") IN ('park slope') AND "listings"."price">=155 AND "listings"."price"<=155 AND "listings"."min_nights">=5 AND "listings"."availability">=189 AND "hosts"."num_of_listings">=1 AND LOWER("listings"."room_type") IN ('entire home/apt') LIMIT 1000'''
        actual_query = Listing().build_get_all_query(given_filter).get_sql()
        # expected query matches actual query
        self.assertEqual(expected_query, actual_query)

    #########################################
    #   'build_get_all_by_id_query' tests   #
    #########################################
    def test_build_get_all_by_id_query(self):
        # build_get_all_by_id_query
        given_ids = [1, 2, 3]
        expected_query = '''SELECT "listings"."id","listings"."name","listings"."neighbourhood","listings"."area","listings"."longitude","listings"."latitude","listings"."room_type" "roomType","listings"."price","listings"."min_nights" "minNights","listings"."num_of_reviews" "numOfReviews","listings"."availability","hosts"."id" "host_id","hosts"."name" "host_name","hosts"."num_of_listings" FROM "listings" JOIN "hosts" ON "listings"."host_id"="hosts"."id" WHERE "listings"."id" IN (1,2,3)'''
        actual_query = Listing().build_get_all_by_id_query(given_ids).get_sql()
        # expected query matches actual query
        self.assertEqual(expected_query, actual_query)

    ########################
    #   Test: get_metadata    #
    ########################
    def test_get_metadata(self):
        metadata = Listing().get_metadata()
        self.assertTrue(metadata)