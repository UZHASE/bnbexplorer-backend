import random

import connexion
import six
from flask import jsonify

from swagger_server.models.host import Host  # noqa: E501
from swagger_server import util


def find_host_by_id(hostId):  # noqa: E501
    """Find Hosts by ID

    Returns a single Host matching the given ID # noqa: E501

    :param hostId: ID of Host to return
    :type hostId: int

    :rtype: List[Host]
    """
    host = Host(hostId, 'Host', random.randint(0, 10))
    return jsonify(host)
