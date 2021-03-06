# coding: utf-8

from __future__ import absolute_import

from test import BaseTestCase


class TestLayersController(BaseTestCase):
    """LayersController integration test stubs"""

    def test_find_complaints_layer(self):
        """Test case for find_complaints_layer

        Retrieve Complaints Layer details
        """
        response = self.client.open(
            '/api/v1/airbnb-explorer/layers/complaints',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_crime_layer(self):
        """Test case for find_crime_layer

        Retrieve Crime Layer details
        """
        response = self.client.open(
            '/api/v1/airbnb-explorer/layers/crime',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_health_layer(self):
        """Test case for find_health_layer

        Retrieve Health Layer details
        """
        response = self.client.open(
            '/api/v1/airbnb-explorer/layers/health',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
