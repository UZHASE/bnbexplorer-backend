from unittest import TestCase

from server.repositories.host_repository import Host


class TestHost(TestCase):

    ########################
    #   Test: get_by_id    #
    ########################
    def test_get_by_id_successful(self):
        given_id = 7351
        hosts = Host().get_by_id(given_id)

        self.assertEqual(1, len(hosts))
        self.assertEqual(given_id, hosts[0].id)
        self.assertIsInstance(hosts[0].id, int)
        self.assertIsInstance(hosts[0].name, str)
        self.assertIsInstance(hosts[0].num_of_listings, int)

    def test_get_by_id_not_found(self):
        given_id = -1
        hosts = Host().get_by_id(given_id)

        self.assertEqual(0, len(hosts))