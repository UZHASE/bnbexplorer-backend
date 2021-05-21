from server.repositories.base_repository import Repository


class Layer(Repository):
    """Repository for Layer object access"""

    def __init__(self, strategy):
        """
        Use constructor to set layer strategy
        """
        super().__init__()
        self._strategy = strategy

    def get_all(self):
        """ Retrieve all Layer information to be used for Heatmaps

        :return: Layer containing Heatmap data
        :rtype: Layer
        """
        # build query
        query = self._build_get_all_query()
        # execute query
        return self._execute_select_query(query)

    def _build_get_all_query(self):
        """ Build query to retrieve all Layer data based on the specified layer strategy

        :return: SQL query ready to be executed
        """
        # delegate to strategy
        return self._strategy._build_get_all_query()

    def _map_result(self, query_results):
        """ Maps a SQL query result (row) to Layer object

        :param query_results: SQL query result (row)
        :return: the resulting Layer
        :rtype: Layer
        """
        # delegate to strategy
        return self._strategy._map_result(query_results)
