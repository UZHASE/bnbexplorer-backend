import connexion
import six
from flask import jsonify

from swagger_server.models.listing import Listing  # noqa: E501
from swagger_server.models.review import Review  # noqa: E501
from swagger_server import util


def find_listing_by_id(listingId):  # noqa: E501
    """Find Listing by ID

    Returns a single Listing matching the given ID # noqa: E501

    :param listingId: ID of Listing to return
    :type listingId: int

    :rtype: Listing
    """
    listing = Listing(
        listingId,
        'Listing',
        'Host',
        'Brooklyn',
        'Midtown',
        47.3769,
        8.5417,
        'Single Room',
        123,
        1,
        3333,
        365
    )
    return jsonify(listing)


def find_listings(listingName=None, hostId=None, hostName=None, location=None, area=None, priceMin=None, priceMax=None, minNights=None, availability=None, listingsPerHost=None, roomType=None):  # noqa: E501
    """Retrieve NYC AirBnB listings

    Returns a list of AirBnB Listings based on the provided filter criteria # noqa: E501

    :param listingName: Name to match Listings (can bei either exact match or not)
    :type listingName: int
    :param hostId: Filter Listings based on hostId
    :type hostId: int
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
    listing1 = Listing(
        1,
        'Listing',
        'Host',
        'Brooklyn',
        'Midtown',
        47.3769,
        8.5417,
        'Single Room',
        123,
        1,
        3333,
        365
    )

    listing2 = Listing(
        2,
        'Listing',
        'Host',
        'Brooklyn',
        'Midtown',
        47.3769,
        8.5417,
        'Single Room',
        123,
        1,
        3333,
        365
    )
    return jsonify(listing1, listing2)


def find_reviews_for_listing(listingId):  # noqa: E501
    """Find Reviews for a given Listing

    Returns all Reviews for a single Listing matching the given ID # noqa: E501

    :param listingId: ID of Listing to return Reviews
    :type listingId: int

    :rtype: List[Review]
    """
    review1 = Review(
        1,
        listingId,
        'Very nice!'
    )

    review2 = Review(
        2,
        listingId,
        'Good!'
    )

    review3 = Review(
        3,
        listingId,
        'Worst AirBnB ever!'
    )

    return jsonify(review1, review2, review3)
