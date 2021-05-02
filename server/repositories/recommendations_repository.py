import math
import random
from pypika import Query
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

from server.dbutils.map_rt import MapRT
from server.repositories.base_repository import Repository
from server.repositories.listing_repsotory import Listing as Listing_Repository
from server.utils.validation import no_none_args


class RecommendationsRepository(Repository):

    @no_none_args
    def recommend_n_listings(self, listing_id, request_filter, n=5):
        """ Recommend n Listings factoring in the provided filter criteria

        :param listing_id: Listing ID of target
        :param request_filter: filter criteria
        :param n: number of recommendations to compute
        :return: recommended Listings
        :raises ValueError: if no ID or filter was provided or n < 1
        """
        # precondition
        if n < 1:
            raise ValueError('Number of recommendations to compute must be at least 1')
        # query building
        listing_query = Query \
            .from_(self.listings) \
            .select(
                # the relevant fields to compute row similarity (encode room_type)
                self.listings.id, self.listings.longitude, self.listings.latitude,
                MapRT(self.listings.room_type).as_('room_type'), self.listings.price,
                self.listings.min_nights, self.listings.num_of_reviews, self.listings.availability
            )
        # add filter criteria
        listing_query = Listing_Repository().add_where_clauses(listing_query, request_filter)
        # execute query
        listings_dict = self.execute_select_query(listing_query.get_sql())
        # compute recommendations and get their IDs
        rec_ids = self.compute_n_recommendations(listings_dict, listing_id, n)
        # fetch listings
        return Listing_Repository().get_all_by_id(rec_ids)

    @no_none_args
    def compute_n_recommendations(self, listings_dict, target_id, n):
        """ Computes n recommendations for a given target Listing

        :param listings_dict: Listings returned based on filter criteria
        :param target_id: ID of Listing
        :param n: number of recommendations
        :return: IDs of recommendations
        :raises ValueError: if filter criteria was too restrictive or target cannot be found
        """
        # precondition
        try:
            # keep track of ids and target index which we need to retrieve recommendations
            id_list = list(listings_dict.keys())
            target_idx = id_list.index(target_id)
        except ValueError:
            raise ValueError('Target Listing with ID {} cannot be found'.format(target_id))

        # scale rows between [0,1]
        scaled_rows = MinMaxScaler().fit_transform(list(listings_dict.values()))
        # compute euclidean distance of each row to target
        [self.euclidean_distance(row, scaled_rows[target_idx]) for row in scaled_rows]
        # compute recommendations: We want to compute more recommendations and then randomly sample a subset
        # first element is target itself, therefore we compute one additional rec.
        k = n * 4 + 1
        if k > len(listings_dict):
            # k must not exceed number of listings
            k = len(listings_dict)
        rec_idx = NearestNeighbors(n_neighbors=k, algorithm='ball_tree') \
            .fit(scaled_rows) \
            .kneighbors([scaled_rows[target_idx]], k, return_distance=False)
        # gather index of recommendations
        rec_ids = []
        for rec in rec_idx[0]:
            rec_ids.append(id_list[rec])
        # randomly sample n (excluding the target itself)
        return random.sample(rec_ids[1:], n)

    @no_none_args
    def euclidean_distance(self, target, row):
        """Computes euclidean distance between target and a given row.
        Formula: ∑ √(A - B)^2 , where A and B are useful values in a given target and row
        :param target: target row to compute distance
        :param row: a row of our data
        :return: euclidean distance to target row
        """
        distance = 0
        index = 0
        for val in row:
            distance += (val - target[index]) ** 2
            index += 1
        return math.sqrt(distance)

    @no_none_args
    def map_result(self, query_result):
        # object mapping
        ids = []
        rows = []
        for row in query_result:
            ids.append((row[0]))
            rows.append(list(row[1:]))
        return dict(zip(ids, rows))
