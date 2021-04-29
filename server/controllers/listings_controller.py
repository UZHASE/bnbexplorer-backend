from flask import jsonify

from server.models.listings_filter import ListingsFilter
from server.repositories.listing_repsotory import Listing as Listing_Repository
from server.repositories.review_repsotory import Review as Review_Repository


def find_listing_by_id(listing_id):
    """Find Listing by ID

    Returns a single Listing matching the given ID

    :param listing_id: ID of Listing to return
    :type listing_id: int

    :rtype: Listing
    """
    return jsonify(Listing_Repository().get_by_id(listing_id))


def find_listings(listing_name=None, host_id=None, host_name=None, location=None, area=None, price_min=None,
                  price_max=None, min_nights=None, availability=None, listings_per_host=None,
                  room_type=None):  # noqa: E501
    """Retrieve NYC AirBnB listings

    Returns a list of AirBnB Listings based on the provided filter criteria # noqa: E501

    :param listing_name: Name to match Listings (can bei either exact match or not)
    :type listing_name: str
    :param host_id: Filter Listings based on hostId
    :type host_id: int
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
    # provided filter options
    request_filter = ListingsFilter(
        listing_name,
        host_id,
        host_name,
        location,
        area,
        price_min,
        price_max,
        min_nights,
        availability,
        listings_per_host,
        room_type
    )
    return jsonify(Listing_Repository().get_all(request_filter))


def find_reviews_for_listing(listing_id):
    """Find Reviews for a given Listing

    Returns all Reviews for a single Listing matching the given ID # noqa: E501

    :param listing_id: ID of Listing to return Reviews
    :type listing_id: int

    :rtype: List[Review]
    """

    return jsonify(Review_Repository().get_all_by_listing_id(listing_id))

def metadata():

    return 'Return some metadata'
