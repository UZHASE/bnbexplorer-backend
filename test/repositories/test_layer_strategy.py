from unittest import TestCase

from server.repositories.layer_strategy import HealthLayerStrategy, CrimeLayerStrategy


class TestLayerStrategy(TestCase):

    def test_health_layer_build_get_all_query(self):
        expected_query = 'SELECT "latitude","longitude" FROM "rat_sightings"'
        actual_query = HealthLayerStrategy()._build_get_all_query()
        self.assertEqual(expected_query, actual_query)

    def test_crime_layer_build_get_all_query(self):
        expected_query = 'SELECT "latitude","longitude" FROM "nypd_incidents" WHERE "crime_type"<>\'OFF. AGNST PUB ORD SENSBLTY &\''
        actual_query = CrimeLayerStrategy()._build_get_all_query()
        self.assertEqual(expected_query, actual_query)
