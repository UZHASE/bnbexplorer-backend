import random

import connexion
import six
from flask import jsonify

from swagger_server.models.host import Host  # noqa: E501
from swagger_server import util
from swagger_server.repositories.host_repository import Host as Host_Repository


def find_host_by_id(host_id):  # noqa: E501
    """Find Hosts by ID

    Returns a single Host matching the given ID # noqa: E501

    :param host_id: ID of Host to return
    :type host_id: int

    :rtype: List[Host]
    """
    return jsonify(Host_Repository().get_by_id(host_id))
