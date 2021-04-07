import os
import sqlite3


class Repository(object):
    # set row limit (temporary)
    ROW_LIMIT = 1000

    def __init__(self):
        self.__connection = sqlite3.connect(str(os.environ.get('DB_PATH', 'database/bnbexplorer.sqlite')))
        self.__connection.row_factory = sqlite3.Row
        self._db = self.__connection.cursor()

    def execute_select_query(self, query):
        # execute query
        query_results = self._db.execute(query).fetchall()
        # object mapping
        return self.map_result(query_results)

    def map_result(self, query_result):
        # Must be implemented by subclass
        raise NotImplementedError
