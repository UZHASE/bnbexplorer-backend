# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.listing import Listing  # noqa: E501
from swagger_server.models.review import Review  # noqa: E501
from swagger_server.test import BaseTestCase


class TestListingsController(BaseTestCase):
    """ListingsController integration test stubs"""

    def test_find_listing_by_id(self):
        """Test case for find_listing_by_id

        Find Listing by ID
        """
        response = self.client.open(
            '/api/v1/airbnb-explorer/listings/{listingId}'.format(listingId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_listings(self):
        """Test case for find_listings

        Retrieve NYC AirBnB listings
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
            '/api/v1/airbnb-explorer/listings',
            method='GET',
            query_string=str(query_string))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_reviews_for_listing(self):
        """Test case for find_reviews_for_listing

        Find Reviews for a given Listing
        """
        response = self.client.open(
            '/api/v1/airbnb-explorer/listings/{listingId}/reviews'.format(listingId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()