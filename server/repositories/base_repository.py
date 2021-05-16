import os
import sqlite3

from pypika import Table


class Repository(object):
    """Repository base class defining common methods
    """
    # tables
    listings = Table('listings')
    hosts = Table('hosts')
    # set row limit (temporary)
    ROW_LIMIT = 1000

    def __init__(self):
        self.__connection = sqlite3.connect(str(os.environ.get('DB_PATH', 'database/bnbexplorer.sqlite')))
        # register SQLite custom function
        self.__connection.create_function('map_rt', 1, self.map_rt)
        self.__connection.row_factory = sqlite3.Row
        self._db = self.__connection.cursor()

    def map_rt(self, room_type):
        """Method to map room_type field in a query

        :param room_type: room_type string to map
        :return: numerical encoding of room_type
        """
        if room_type is not None:
            if room_type == 'Private room':
                return 1
            elif room_type == 'Entire home/apt':
                return 2
            elif room_type == 'Shared Room':
                return 3
            else:
                # fallback
                return 0
        else:
            # fallback
            return 0

    def _execute_select_query(self, query):
        """Template method defining the basic procedure for SELECT query execution

        :param query: SELECT query to be executed
        :return: result set of mapped object(s)
        """
        # execute query
        query_results = self._db.execute(query).fetchall()
        # object mapping
        return self._map_result(query_results)

    def _map_result(self, query_result):
        """Defines how to map DB results (rows) to the desired object. Must be implemented by subclass

        :raises NotImplementedError: if not implemented
        """
        # Must be implemented by subclass
        raise NotImplementedError
