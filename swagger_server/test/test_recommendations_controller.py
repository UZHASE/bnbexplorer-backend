# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.listing import Listing  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRecommendationsController(BaseTestCase):
    """RecommendationsController integration test stubs"""

    def test_recommend_listings(self):
        """Test case for recommend_listings

        Recommend AirBnBs based on provided filter criteria
        """
        query_string = [('listingName', 56),
                        ('hostName', 'hostName_example'),
                        ('location', 'location_example'),
                        ('area', 'area_example'),
                        ('priceMin', 56),
                        ('priceMax', 56),
                        ('minNights', 56),
                        ('availability', 56),
                        ('listingsPerHost', 56),
                        ('roomType', 'roomType_example')]
        response = self.client.open(
            '/api/v1/airbnb-explorer/listings/recommendations',
            method='GET',
            query_string=query_string)
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
