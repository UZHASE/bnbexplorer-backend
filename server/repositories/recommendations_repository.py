import math
import random
from pypika import Table, Query
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

from server.dbutils.map_rt import MapRT
from server.repositories.base_repository import Repository
from server.repositories.listing_repsotory import Listing as Listing_Repository


class RecommendationsRepository(Repository):
    # tables
    listings = Table('listings')
    hosts = Table('hosts')

    def recommend_listing(self, listing_id, request_filter):
        # TODO: Testing!
        # query building
        listing_query = Query \
            .from_(self.listings) \
            .select(
                self.listings.id, self.listings.longitude, self.listings.latitude,
                MapRT(self.listings.room_type).as_('room_type'), self.listings.price,
                self.listings.min_nights, self.listings.num_of_reviews, self.listings.availability
            )
        # add filter criteria
        listing_query = Listing_Repository().add_where_clauses(listing_query, request_filter)
        # execute query
        listings_dict = self.execute_select_query(listing_query.get_sql())
        # keep track of ids which we need to retrieve recommendations
        id_list = list(listings_dict.keys())
        rec_ids = []
        if listings_dict:
            target_idx = id_list.index(listing_id)
            # scale rows between [0,1]
            scaled_rows = MinMaxScaler().fit_transform(list(listings_dict.values()))
            # compute euclidean distance compared to target
            [self.euclidean_distance(row, scaled_rows[target_idx]) for row in scaled_rows]
            target_score = scaled_rows[target_idx]
            # compute recommendations: select 20 closest listings and randomly sample 5
            # (first element is target itself!)
            nbrs = NearestNeighbors(n_neighbors=6, algorithm='ball_tree').fit(scaled_rows)
            rec_idx = nbrs.kneighbors([target_score], 21, return_distance=False)
            # gather index of recommendations
            for rec in rec_idx[0]:
                rec_ids.append(id_list[rec])
            # randomly sample 5 (excluding the target itself)
            rec_ids = random.sample(rec_ids[1:], 5)
        # fetch listings
        return Listing_Repository().get_all_by_id(rec_ids)

    def map_result(self, query_result):
        # object mapping
        ids = []
        rows = []
        for row in query_result:
            ids.append((row[0]))
            rows.append(list(row[1:]))
        return dict(zip(ids, rows))

    def euclidean_distance(self, target, row):
        score = 0
        index = 0
        for val in row:
            score += (val - target[index]) ** 2
            index += 1
        return math.sqrt(score)
