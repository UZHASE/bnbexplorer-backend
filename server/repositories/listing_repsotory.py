from pypika import Query, Table
from pypika.functions import Lower

from server.repositories.base_repository import Repository
from server.models.listing import Listing as Listing_Model
from server.models.host import Host as Host_Model


class Listing(Repository):

    def get_by_id(self, listing_id):
        # build query
        listing_query = self.build_get_by_id_query(listing_id)
        # execute query always returns a (singleton ot empty) list, but we need the Listing object
        images = self._db.execute('''SELECT urls FROM listings_images WHERE listing_id = ?''', (listing_id,)).fetchone()
        listing = self.execute_select_query(listing_query.get_sql())

        if listing:
            listing[0].images = images['urls'].split(' ') if images else []
            return listing[0]

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
        # query building
        query = Query \
            .from_(self.listings) \
            .join(self.hosts) \
            .on(self.listings.host_id == self.hosts.id) \
            .select(
                self.listings.id, self.listings.name, self.listings.neighbourhood, self.listings.area,
                self.listings.longitude, self.listings.latitude, self.listings.room_type.as_('roomType'),
                self.listings.price, self.listings.min_nights.as_('minNights'),
                self.listings.num_of_reviews.as_('numOfReviews'), self.listings.availability,
                self.hosts.id.as_('host_id'), self.hosts.name.as_('host_name'), self.hosts.num_of_listings) \
            .where(self.listings.id == listing_id)
        return query

    def build_get_all_by_id_query(self, id_list):
        # query building
        query = Query \
            .from_(self.listings) \
            .join(self.hosts) \
            .on(self.listings.host_id == self.hosts.id) \
            .select(
                self.listings.id, self.listings.name, self.listings.neighbourhood, self.listings.area,
                self.listings.longitude, self.listings.latitude, self.listings.room_type.as_('roomType'),
                self.listings.price, self.listings.min_nights.as_('minNights'),
                self.listings.num_of_reviews.as_('numOfReviews'), self.listings.availability,
                self.hosts.id.as_('host_id'), self.hosts.name.as_('host_name'), self.hosts.num_of_listings) \
            .where(self.listings.id.isin(id_list))
        return query

    def build_get_all_query(self, filter):
        # query building
        query = Query \
            .from_(self.listings) \
            .join(self.hosts) \
            .on(self.listings.host_id == self.hosts.id) \
            .select(
                self.listings.id, self.listings.name, self.listings.neighbourhood, self.listings.area,
                self.listings.longitude, self.listings.latitude, self.listings.room_type.as_('roomType'),
                self.listings.price, self.listings.min_nights.as_('minNights'),
                self.listings.num_of_reviews.as_('numOfReviews'), self.listings.availability,
                self.hosts.id.as_('host_id'), self.hosts.name.as_('host_name'), self.hosts.num_of_listings) \
            .limit(self.ROW_LIMIT)
        return self.add_where_clauses(query, filter)

    def add_where_clauses(self, query, filter):
        # WHERE clauses
        if filter.listing_name:
            query = query.where(Lower(self.listings.name).like(Lower(filter.listing_name + '%')))
        if filter.host_id is not None:
            query = query.where(self.hosts.id == filter.host_id)
        if filter.host_name:
            query = query.where(Lower(self.hosts.name).like(Lower(filter.host_name + '%')))
        if filter.neighbourhood:
            # to lowercase for string comparison
            filter.neighbourhood = [n.lower() for n in filter.neighbourhood]
            query = query.where((Lower(self.listings.neighbourhood)).isin(filter.neighbourhood))
        if filter.area:
            # to lowercase for string comparison
            filter.area = [a.lower() for a in filter.area]
            query = query.where((Lower(self.listings.area)).isin(filter.area))
        if filter.price_min is not None:
            query = query.where(self.listings.price >= filter.price_min)
        if filter.price_max is not None:
            query = query.where(self.listings.price <= filter.price_max)
        if filter.min_nights is not None:
            query = query.where(self.listings.min_nights >= filter.min_nights)
        if filter.availability is not None:
            # TODO: Should this input be handled as an enum, or min/max values? (currently: min value)
            query = query.where(self.listings.availability >= filter.availability)
        if filter.listings_per_host is not None:
            # TODO: Should this input be handled as an enum, or min/max values? (currently: min value)
            query = query.where(self.hosts.num_of_listings >= filter.listings_per_host)
        if filter.room_type:
            # to lowercase for string comparison
            filter.room_type = [a.lower() for a in filter.room_type]
            query = query.where((Lower(self.listings.room_type)).isin(filter.room_type))
        return query

    def get_metadata(self):
        min_max_listings = self._db.execute('''
        SELECT 
            MIN(price) minPrice, 
            MAX(price) maxPrice, 
            COUNT(*) numOfListings 
        FROM listings
        ''').fetchone()

        min_max_hosts = self._db.execute('''
        SELECT 
            MIN(num_of_listings) minListingsPerHost, 
            MAX(num_of_listings) maxListingsPerHost 
        FROM hosts
        ''').fetchone()

        areas = self._db.execute('SELECT DISTINCT(area) areas FROM listings').fetchall()
        neighbourhoods = self._db.execute('SELECT DISTINCT(neighbourhood) neighbourhoods FROM listings').fetchall()
        room_types = self._db.execute('SELECT DISTINCT(room_type) roomTypes FROM listings').fetchall()

        return {
            'minPrice': min_max_listings['minPrice'],
            'maxPrice': min_max_listings['maxPrice'],
            'numOfListings': min_max_listings['numOfListings'],
            'areas': [area[0] for area in areas],
            'neighbourhoods': [neighbourhood[0] for neighbourhood in neighbourhoods],
            'roomTypes': [room_type[0] for room_type in room_types],
            'minListingsPerHost': min_max_hosts['minListingsPerHost'],
            'maxListingsPerHost': min_max_hosts['maxListingsPerHost']
        }


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
