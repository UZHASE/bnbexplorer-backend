import connexion
import six

from swagger_server.models.listing import Listing  # noqa: E501
from swagger_server import util


def recommend_listings(listingName=None, hostName=None, location=None, area=None, priceMin=None, priceMax=None, minNights=None, availability=None, listingsPerHost=None, roomType=None):  # noqa: E501
    """Recommend AirBnBs based on provided filter criteria

    Returns a list of recommended Listings # noqa: E501

    :param listingName: Name to match Listings (can bei either exact match or not)
    :type listingName: int
    :param hostName: Name to match Hosts of Listings (can bei either exact match or not)
    :type hostName: str
    :param location: Filter Listings by their location
    :type location: str
    :param area: Filter Listings by their area
    :type area: str
    :param priceMin: Filter Listings by minimum price
    :type priceMin: int
    :param priceMax: Filter Listings by maximum price
    :type priceMax: int
    :param minNights: Filter Listings by minimum nights
    :type minNights: int
    :param availability: Filter Listings by their availability
    :type availability: int
    :param listingsPerHost: Filter Listings by the number of Listings per Host
    :type listingsPerHost: int
    :param roomType: Filter Listings by room type
    :type roomType: str

    :rtype: List[Listing]
    """
    return 'do some magic!'


def recommend_listings_for_attractions():  # noqa: E501
    """Recommend closest AirBnBs based on a list of Attractions

    Returns a list of recommended Listings # noqa: E501


    :rtype: List[Listing]
    """
    return 'do some magic!'
