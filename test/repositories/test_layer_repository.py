from unittest import TestCase

from server.repositories.layer_repository import Layer
from server.repositories.layer_strategy import HealthLayerStrategy, CrimeLayerStrategy


class TestLayer(TestCase):

    def test_health_layer(self):
        health_layer = Layer(HealthLayerStrategy()).get_all()
        self.assertEqual('HEALTH_LAYER', health_layer.type)
        self.assertTrue(health_layer.entries)

    def test_crime_layer(self):
        crime_layer = Layer(CrimeLayerStrategy()).get_all()
        self.assertEqual('CRIME_LAYER', crime_layer.type)
        self.assertTrue(crime_layer.entries)