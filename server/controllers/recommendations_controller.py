from server.models.listings_filter import ListingsFilter
from server.repositories.recommendations_repository import RecommendationsRepository as Recommendations_Repository


def recommend_listings(listing_id=None, host_id=None, listing_name=None, host_name=None,
                       location=None, area=None, price_min=None, price_max=None, min_nights=None,
                       availability=None, listings_per_host=None, room_type=None):
    """Recommend AirBnBs based on provided filter criteria

    Returns a list of recommended Listings based on a provided Listing and taking filter criteria into account

    :param listing_id: target Listing ID
    :type listing_id: int
    :param host_id: host ID
    :type host_id: int
    :param listing_name: Name to match Listings (can bei either exact match or not)
    :type listing_name: str
    :param host_name: Name to match Hosts of Listings (can bei either exact match or not)
    :type host_name: str
    :param location: Filter Listings by their location
    :type location: list of str
    :param area: Filter Listings by their area
    :type area: list of str
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
    :type room_type: list of str

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
    return Recommendations_Repository().recommend_n_listings(listing_id, request_filter)
