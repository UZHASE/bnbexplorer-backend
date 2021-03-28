# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.layer import Layer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLayersController(BaseTestCase):
    """LayersController integration test stubs"""

    def test_find_complaints_layer(self):
        """Test case for find_complaints_layer

        Retrieve Complaints Layer details
        """
        response = self.client.open(
            '/layers/complaints',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_crime_layer(self):
        """Test case for find_crime_layer

        Retrieve Crime Layer details
        """
        response = self.client.open(
            '/layers/crime',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_health_layer(self):
        """Test case for find_health_layer

        Retrieve Health Layer details
        """
        response = self.client.open(
            '/layers/health',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
