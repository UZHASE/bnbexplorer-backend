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
            '/listings/{listingId}'.format(listing_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_listings(self):
        """Test case for find_listings

        Retrieve NYC AirBnB listings
        """
        query_string = [('listing_name', 56),
                        ('host_id', 56),
                        ('host_name', 'host_name_example'),
                        ('location', 'location_example'),
                        ('area', 'area_example'),
                        ('price_min', 56),
                        ('price_max', 56),
                        ('min_nights', 56),
                        ('availability', 56),
                        ('listings_per_host', 56),
                        ('room_type', 'room_type_example')]
        response = self.client.open(
            '/listings',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_reviews_for_listing(self):
        """Test case for find_reviews_for_listing

        Find Reviews for a given Listing
        """
        response = self.client.open(
            '/listings/{listingId}/reviews'.format(listing_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
