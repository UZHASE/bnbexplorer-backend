# coding: utf-8

from __future__ import absolute_import

from test import BaseTestCase


class TestRecommendationsController(BaseTestCase):
    """RecommendationsController integration test stubs"""

    def test_recommend_listings(self):
        """Test case for recommend_listings

        Recommend AirBnBs based on provided filter criteria
        """
        query_string = [('listing_name', 'Test'),
                        ('host_id', 56),
                        ('host_name', 'Host'),
                        ('location', 'Manhattan'),
                        ('area', 'Midtown'),
                        ('price_min', 56),
                        ('price_max', 56),
                        ('min_nights', 56),
                        ('availability', 365),
                        ('listings_per_host', 56),
                        ('room_type', 'Single Room')]
        response = self.client.open(
            '/api/v1/airbnb-explorer/listings/recommendations',
            method='GET',
            query_string=str(query_string))
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
