from pypika import Query, Table

from server.repositories.base_repository import Repository
from server.models.review import Review as Review_Model


class Review(Repository):

    def get_all_by_listing_id(self, listing_id):
        query = self.build_get_all_by_listing_id_query(listing_id)

        return self.execute_select_query(query)

    def build_get_all_by_listing_id_query(self, listing_id):
        reviews = Table('reviews')

        return Query\
            .from_(reviews)\
            .select(
                reviews.id,
                reviews.listing_id.as_('listingId'),
                reviews.comments.as_('text'))\
            .where(reviews.listing_id == listing_id)\
            .get_sql()

    def map_result(self, query_results):
        return [Review_Model.from_dict(dict(row)) for row in query_results]