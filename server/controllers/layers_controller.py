import connexion
import six
from flask import jsonify

from server.models.layer import Layer
from server.repositories.layer_repository import Layer as Layer_Repository
from server import util
from server.repositories.layer_strategy import CrimeLayerStrategy, HealthLayerStrategy


def find_complaints_layer():
    """Retrieve Complaints Layer details

    Returns details to diyplay Complaints Layer (amount per neighbourhood)


    :rtype: Layer
    """
    return 'do some magic!'


def find_crime_layer():
    """Retrieve Crime Layer details

    Returns details to diyplay Crime Layer (amount per neighbourhood)


    :rtype: Layer
    """
    return jsonify(Layer_Repository(CrimeLayerStrategy()).get_all())


def find_health_layer():
    """Retrieve Health Layer details

    Returns details to diyplay Health Layer (amount per neighbourhood)


    :rtype: Layer
    """
    return jsonify(Layer_Repository(HealthLayerStrategy()).get_all())
