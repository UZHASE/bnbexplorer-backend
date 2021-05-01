# coding: utf-8

from __future__ import absolute_import

from test import BaseTestCase


class TestRecommendationsController(BaseTestCase):
    """RecommendationsController integration test stubs"""

    def test_recommend_listings(self):
        """Test case for recommend_listings

        Recommend AirBnBs based on provided filter criteria
        """
        response = self.client.open(
            '/api/v1/airbnb-explorer/listings/recommendations?listingId=2539',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_recommend_listings_for_attractions(self):
        """Test case for recommend_listings_for_attractions

        Recommend closest AirBnBs based on a list of Attractions
        """
        response = self.client.open(
            '/api/v1/airbnb-explorer/listings/attractions',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
