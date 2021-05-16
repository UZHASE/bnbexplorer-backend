from pypika import Query, Table

from server.repositories.base_repository import Repository
from server.models.review import Review as Review_Model


class Review(Repository):
    """ Repository for Review object access"""

    def get_all_by_listing_id(self, listing_id):
        """ Retrieve all Reviews for a given Listing ID

        :param listing_id: ID of a Listing
        :return: all reviews for a given Listing
        :rtype: List[Review]
        """
        query = self._build_get_all_by_listing_id_query(listing_id)
        return self._execute_select_query(query)

    def _build_get_all_by_listing_id_query(self, listing_id):
        """ Build query to retrieve Reviews for a given Listing ID

        :param listing_id: ID of Listing
        :return: SQL query ready to be executed
        """
        reviews = Table('reviews')

        return Query\
            .from_(reviews)\
            .select(
                reviews.id,
                reviews.listing_id.as_('listingId'),
                reviews.comments.as_('text'))\
            .where(reviews.listing_id == listing_id)\
            .get_sql()

    def _map_result(self, query_results):
        """ Maps a SQL query result (row) to Review objects

        :param query_results: SQL query result (row)
        :return: resulting List of Reviews
        :rtype: List[Review]
        """
        return [Review_Model.from_dict(dict(row)) for row in query_results]