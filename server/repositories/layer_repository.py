from server.repositories.base_repository import Repository


class Layer(Repository):

    def __init__(self, strategy):
        """
        Use constructor to set layer strategy
        """
        super().__init__()
        self._strategy = strategy

    def get_all(self):
        # build query
        query = self.build_get_all_query()
        # execute query
        return self.execute_select_query(query)

    def build_get_all_query(self):
        # delegate to strategy
        return self._strategy.build_get_all_query()

    def map_result(self, query_results):
        # delegate to strategy
        return self._strategy.map_result(query_results)
