class ListingsFilter:
    def __init__(self, listing_name=None, host_id=None, host_name=None,
                 neighbourhood=None, area=None, price_min=None, price_max=None,
                 min_nights=None, availability=None, listings_per_host=None, room_type=None):
        """ListingsFilter - filter options to query Listings

        :param listing_name: Filter by Listing name
        :type listing_name: str
        :param host_id: Filter by Host ID
        :type host_id: int
        :param host_name: Filter by Host name
        :type host_name: str
        :param neighbourhood:  Filter by neighbourhood of Listing
        :type neighbourhood: str
        :param area: Filter by area of Listing
        :type area: str
        :param price_min: Filter by min price of Listings
        :type price_min: int
        :param price_max: Filter by max price of Listings
        :type price_max: int
        :param min_nights: Filter by min nights for Listings
        :type min_nights: int
        :param availability: Filter by availability of Listings
        :type availability: int
        :param listings_per_host: Filter by number of Listings per Host
        :type listings_per_host: int
        :param room_type: Filter by room type of Listings
        :type room_type: str
         """
        self.listing_name = listing_name
        self.host_id = host_id
        self.host_name = host_name
        self.neighbourhood = neighbourhood
        self.area = area
        self.price_min = price_min
        self.price_max = price_max
        self.min_nights = min_nights
        self.availability = availability
        self.listings_per_host = listings_per_host
        self.room_type = room_type
