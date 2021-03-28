import connexion
import six

from swagger_server.models.listing import Listing  # noqa: E501
from swagger_server import util


def recommend_listings(listing_name=None, host_name=None, location=None, area=None, price_min=None, price_max=None, min_nights=None, availability=None, listings_per_host=None, room_type=None):  # noqa: E501
    """Recommend AirBnBs based on provided filter criteria

    Returns a list of recommended Listings # noqa: E501

    :param listing_name: Name to match Listings (can bei either exact match or not)
    :type listing_name: int
    :param host_name: Name to match Hosts of Listings (can bei either exact match or not)
    :type host_name: str
    :param location: Filter Listings by their location
    :type location: str
    :param area: Filter Listings by their area
    :type area: str
    :param price_min: Filter Listings by minimum price
    :type price_min: int
    :param price_max: Filter Listings by maximum price
    :type price_max: int
    :param min_nights: Filter Listings by minimum nights
    :type min_nights: int
    :param availability: Filter Listings by their availability
    :type availability: int
    :param listings_per_host: Filter Listings by the number of Listings per Host
    :type listings_per_host: int
    :param room_type: Filter Listings by room type
    :type room_type: str

    :rtype: List[Listing]
    """
    return 'do some magic!'


def recommend_listings_for_attractions():  # noqa: E501
    """Recommend closest AirBnBs based on a list of Attractions

    Returns a list of recommended Listings # noqa: E501


    :rtype: List[Listing]
    """
    return 'do some magic!'
