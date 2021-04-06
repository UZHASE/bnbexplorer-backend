from pypika import Query, Table, Schema

from server.repositories.base_repository import Repository
from server.models.listing import Listing as Listing_Model
from server.models.host import Host as Host_Model


class Listing(Repository):

    def get_all(self, listings_filter):

        # build query with provided params
        query = self.build_query(listings_filter)
        # execute query
        query_results = self._db.execute(query).fetchall()
        # object mapping
        result = []
        for row in query_results:
            row = dict(row)
            listing = Listing_Model.from_dict(row)
            listing.host = Host_Model(
                id=row['host_id'],
                name=row['host_name'],
                num_of_listings=row['num_of_listings']
            )
            result.append(listing)

        return result

    def build_query(self, filter):
        # tables
        listings = Table('listings')
        hosts = Table('hosts')
        # query building
        query = Query \
            .from_(listings) \
            .from_(hosts) \
            .select(
                listings.id, listings.name, listings.neighbourhood, listings.area, listings.longitude, listings.latitude,
                listings.room_type.as_('roomType'), listings.price, listings.min_nights.as_('minNights'),
                listings.num_of_reviews.as_('numOfReviews'), listings.availability, hosts.id.as_('host_id'),
                hosts.name.as_('host_name'), hosts.num_of_listings)
        # WHERE clauses
        if filter.listing_name is not None:
            # TODO: Does not need to be exact match, we could SQL's LIKE function for partial matching
            query = query.where(listings.name == filter.listing_name)
        if filter.host_id is not None:
            query = query.where(hosts.id == filter.host_id)
        if filter.host_name is not None:
            # TODO: Does not need to be exact match, we could SQL's LIKE function for partial matching
            query = query.where(hosts.name == filter.host_name)
        if filter.neighbourhood is not None:
            # TODO: We can accept a list and use SQL's IN function to filter for the given values
            query = query.where(listings.neighbourhood == filter.neighbourhood)
        if filter.area is not None:
            # TODO: We can accept a list and use SQL's IN function to filter for the given values
            query = query.where(listings.area == filter.area)
        if filter.price_min is not None:
            query = query.where(listings.price >= filter.price_min)
        if filter.price_max is not None:
            query = query.where(listings.price <= filter.price_max)
        if filter.min_nights is not None:
            query = query.where(listings.min_nights >= filter.min_nights)
        if filter.availability is not None:
            # TODO: Should this input be handled as an enum, or min/max values? (currently: min value)
            query = query.where(listings.availability >= filter.availability)
        if filter.listings_per_host is not None:
            # TODO: Should this input be handled as an enum, or min/max values? (currently: min value)
            query = query.where(hosts.num_of_listings >= filter.listings_per_host)
        if filter.room_type is not None:
            # TODO: We can accept a list and use SQL's IN function to filter for the given values
            query = query.where(listings.room_type == filter.room_type)
        # LIMIT clause
        query = query.limit(self.ROW_LIMIT)

        return str(query)
