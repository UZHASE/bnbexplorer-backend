import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server import util

def get_all_listings():
    return ['listing 1', 'listing 2', 'listing 3']
