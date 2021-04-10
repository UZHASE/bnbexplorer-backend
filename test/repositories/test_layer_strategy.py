from unittest import TestCase

from server.repositories.layer_strategy import HealthLayerStrategy, CrimeLayerStrategy


class TestLayerStrategy(TestCase):

    def test_health_layer_build_get_all_query(self):
        expected_query = 'SELECT "latitude","longitude" FROM "rat_sightings"'
        actual_query = HealthLayerStrategy().build_get_all_query()
        self.assertEqual(expected_query, actual_query)

    def test_crime_layer_build_get_all_query(self):
        expected_query = 'SELECT "latitude","longitude" FROM "nypd_incidents"'
        actual_query = CrimeLayerStrategy().build_get_all_query()
        self.assertEqual(expected_query, actual_query)
