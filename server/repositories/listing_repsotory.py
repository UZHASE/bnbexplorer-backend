import logging

from pypika import Query, Table
from pypika.functions import Lower

from server.repositories.base_repository import Repository
from server.models.listing import Listing as Listing_Model
from server.models.host import Host as Host_Model


class Listing(Repository):

    def get_by_id(self, listing_id):
        # build query
        query = self.build_get_by_id_query(listing_id)
        # execute query always returns a (singleton ot empty) list, but we need the Listing object
        listing = self.execute_select_query(query.get_sql())
        if listing:
            # we have a match, unpack the Listing
            listing = listing[0]
        return listing

    def get_all_by_id(self, id_list):
        # build query
        query = self.build_get_all_by_id_query(id_list)
        # execute query
        return self.execute_select_query(query.get_sql())

    def get_all(self, listings_filter):
        # build query
        query = self.build_get_all_query(listings_filter)
        # execute query
        return self.execute_select_query(query.get_sql())

    def build_get_by_id_query(self, listing_id):
        # tables
        listings = Table('listings')
        hosts = Table('hosts')
        # query building
        query = Query \
            .from_(listings) \
            .join(hosts) \
            .on(listings.host_id == hosts.id) \
            .select(
                listings.id, listings.name, listings.neighbourhood, listings.area, listings.longitude, listings.latitude,
                listings.room_type.as_('roomType'), listings.price, listings.min_nights.as_('minNights'),
                listings.num_of_reviews.as_('numOfReviews'), listings.availability, hosts.id.as_('host_id'),
                hosts.name.as_('host_name'), hosts.num_of_listings) \
            .where(listings.id == listing_id)
        return query

    def build_get_all_by_id_query(self, id_list):
        # TODO: Testing!
        # tables
        listings = Table('listings')
        hosts = Table('hosts')
        # query building
        query = Query \
            .from_(listings) \
            .join(hosts) \
            .on(listings.host_id == hosts.id) \
            .select(
                listings.id, listings.name, listings.neighbourhood, listings.area, listings.longitude, listings.latitude,
                listings.room_type.as_('roomType'), listings.price, listings.min_nights.as_('minNights'),
                listings.num_of_reviews.as_('numOfReviews'), listings.availability, hosts.id.as_('host_id'),
                hosts.name.as_('host_name'), hosts.num_of_listings) \
            .where(listings.id.isin(id_list))
        return query

    def build_get_all_query(self, filter):
        # tables
        listings = Table('listings')
        hosts = Table('hosts')
        # query building
        query = Query \
            .from_(listings) \
            .join(hosts) \
            .on(listings.host_id == hosts.id) \
            .select(
                listings.id, listings.name, listings.neighbourhood, listings.area, listings.longitude, listings.latitude,
                listings.room_type.as_('roomType'), listings.price, listings.min_nights.as_('minNights'),
                listings.num_of_reviews.as_('numOfReviews'), listings.availability, hosts.id.as_('host_id'),
                hosts.name.as_('host_name'), hosts.num_of_listings)
        # WHERE clauses
        if filter.listing_name is not None:
            query = query.where(Lower(listings.name).like(Lower(filter.listing_name + '%')))
        if filter.host_id is not None:
            query = query.where(hosts.id == filter.host_id)
        if filter.host_name is not None:
            query = query.where(Lower(hosts.name).like(Lower(filter.host_name + '%')))
        if filter.neighbourhood is not None:
            # TODO: We can accept a list and use SQL's IN function to filter for the given values
            query = query.where(Lower(listings.neighbourhood) == Lower(filter.neighbourhood))
        if filter.area is not None:
            # TODO: We can accept a list and use SQL's IN function to filter for the given values
            query = query.where(Lower(listings.area) == Lower(filter.area))
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
            query = query.where(Lower(listings.room_type) == Lower(filter.room_type))
        # LIMIT clause
        query = query.limit(self.ROW_LIMIT)
        return query

    def map_result(self, query_results):
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
