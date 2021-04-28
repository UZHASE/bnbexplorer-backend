import random

from pypika import Table, Query, Order
from heapq import nsmallest
from pypika.functions import Sqrt
from pypika.terms import Pow

from server.dbutils.max import Max
from server.dbutils.min import Min
from server.dbutils.normalize import Normalize
from server.models.room_type_mapper import RoomType
from server.repositories.base_repository import Repository
from server.models.listing_distance import ListingDistance as Distance_Model
from server.repositories.listing_repsotory import Listing as Listing_Repository


class RecommendationsRepository(Repository):

    def recommend_listing(self, listing_id, request_filter):
        # TODO: Testing!
        # tables
        listings = Table('listings')
        # query building (similar to listing repo: get_all query)
        subquery_rt = Listing_Repository().build_get_all_query(request_filter)\
                .select(RoomType(listings.room_type).as_('room_type') # with the addition of room_type mapping
            ).as_('rt')

        subquery = Query\
            .from_(subquery_rt)\
            .select(
                subquery_rt.id,
                # normalize values between [0,1]
                Normalize(subquery_rt.longitude, Min(subquery_rt.longitude), Max(subquery_rt.longitude)).as_('long_norm'),
                Normalize(subquery_rt.latitude, Min(subquery_rt.latitude), Max(subquery_rt.latitude)).as_('lat_norm'),
                Normalize(subquery_rt.room_type, Min(subquery_rt.room_type),Max(subquery_rt.room_type)).as_('rt_norm'),
                Normalize(subquery_rt.price, Min(subquery_rt.price), Max(subquery_rt.price)).as_('price_norm'),
                Normalize(subquery_rt.minNights, Min(subquery_rt.minNights), Max(subquery_rt.minNights)).as_('mn_norm'),
                Normalize(subquery_rt.numOfReviews, Min(subquery_rt.numOfReviews), Max(subquery_rt.numOfReviews)).as_('nor_norm'),
                Normalize(subquery_rt.availability, Min(subquery_rt.availability), Max(subquery_rt.availability)).as_('ava_norm')
            ).as_('sq')

        query = Query \
            .from_(subquery) \
            .select(
                subquery.id,
                (Sqrt(
                    Pow(subquery.long_norm, 2) + Pow(subquery.lat_norm, 2) + Pow(subquery.rt_norm, 2) +
                    Pow(subquery.price_norm, 2) + Pow(subquery.mn_norm, 2) + Pow(subquery.nor_norm, 2)
                    + Pow(subquery.ava_norm, 2)
                )).as_('euclidean')
            ).orderby(2, order=Order.desc)
        # TODO: Error handling!
        listing_dists = self.execute_select_query(query.get_sql())
        target_listing = [x for x in listing_dists if x.id == listing_id]
        # correction for missing values
        for listing in listing_dists:
            if listing.euclidean is None:
                # could not be mapped
                listing.euclidean = -1

        recommendations = []
        if listing_dists:
            # shuffle list because in case of equal distances, position matters
            random.shuffle(listing_dists)
            # get the 6 most similar listings to the target (we ignore the first result because it is the target itself)
            recommendations = nsmallest(6, listing_dists, key=lambda x: abs(x.euclidean - target_listing[0].euclidean))[1:]
        # gather ids of recommendations
        id_list = []
        for listing in recommendations:
            id_list.append(listing.id)
        # fetch listings
        return Listing_Repository().get_all_by_id(id_list)

    def map_result(self, query_result):
        # object mapping
        result = []
        for row in query_result:
            row = dict(row)
            listing_distance = Distance_Model.from_dict(row)
            result.append(listing_distance)
        return result
