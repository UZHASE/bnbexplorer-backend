from unittest import TestCase

from server.repositories.layer_repository import Layer
from server.repositories.layer_strategy import HealthLayerStrategy, CrimeLayerStrategy, ComplaintLayerStrategy


class TestLayer(TestCase):

    def test_health_layer(self):
        health_layer = Layer(HealthLayerStrategy()).get_all()
        self.assertEqual('HEALTH_LAYER', health_layer.type)
        self.assertTrue(health_layer.entries)

    def test_crime_layer(self):
        crime_layer = Layer(CrimeLayerStrategy()).get_all()
        self.assertEqual('CRIME_LAYER', crime_layer.type)
        self.assertTrue(crime_layer.entries)

    def test_complaint_layer(self):
        complaint_layer = Layer(ComplaintLayerStrategy()).get_all()
        self.assertEqual('COMPLAINT_LAYER', complaint_layer.type)
        self.assertEqual(554, len(complaint_layer.entries))