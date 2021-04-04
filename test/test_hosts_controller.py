# coding: utf-8

from __future__ import absolute_import

from test import BaseTestCase


class TestHostsController(BaseTestCase):
    """HostsController integration test stubs"""

    def test_find_host_by_id(self):
        """Test case for find_host_by_id

        Find Hosts by ID
        """
        response = self.client.open(
            '/api/v1/airbnb-explorer/hosts/{hostId}'.format(hostId=2787),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
