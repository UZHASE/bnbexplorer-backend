from server.repositories.base_repository import Repository
from server.models.host import Host as Host_Model
from pypika import Query


class Host(Repository):
    """Repository for Host object access"""

    def get_by_id(self, host_id):
        """ Retrieve a single Host by ID

        :param host_id: ID of Host
        :return: Host matching the given ID
        :rtype: Host
        """
        query = self._build_get_by_id_query(host_id)
        return self._execute_select_query(query)

    def _build_get_by_id_query(self, host_id):
        """ Build query to retrieve a Host by its ID

        :param host_id: ID of Host
        :return: SQL query ready to be executed
        """
        return Query\
            .from_(self.hosts)\
            .select(self.hosts.id, self.hosts.name, self.hosts.num_of_listings.as_('numOfListings'))\
            .where(self.hosts.id == host_id)\
            .get_sql()

    def _map_result(self, query_results):
        """ Maps a SQL query result (row) to Host object

        :param query_results: SQL query result (row)
        :return: the resulting Host
        :rtype: Host
        """
        return [Host_Model.from_dict(dict(row)) for row in query_results]
