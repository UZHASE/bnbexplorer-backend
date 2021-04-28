import math
import os
import sqlite3


class Repository(object):
    # set row limit (temporary)
    ROW_LIMIT = 1000

    def __init__(self):
        self.__connection = sqlite3.connect(str(os.environ.get('DB_PATH', 'database/bnbexplorer.sqlite')))
        # TODO: Move the following lines
        self.__connection.create_function('sqrt', 1, self.sqrt)
        self.__connection.create_function('pow', 2, self.power)
        self.__connection.create_function('norm', 3, self.norm)
        self.__connection.create_function('map_rt', 1, self.map_rt)
        self.__connection.create_function('min', 1, self.min)
        self.__connection.create_function('max', 1, self.max)
        self.__connection.row_factory = sqlite3.Row
        self._db = self.__connection.cursor()

    def min(self, col):
       return "MIN({}) OVER()".format(col)

    def max(self, col):
        return "MAX({}) OVER()".format(col)

    def power(self, x, y):
        try:
            if x is not None and x != 0:
                return math.pow(x, y)
            else:
                return 0
        except:
            return 0

    def sqrt(self, x):
        try:
            return math.sqrt(x)
        except:
            # operation is not possible
            return 0

    def norm(self, val, min, max):
        try:
            return (1.00 * val - min) / (max - min)
        except:
            return 0

    def map_rt(self, room_type):
        try:
            if room_type is not None:
                if room_type == 'Private room':
                    return 1
                elif room_type == 'Entire home/apt':
                    return 2
                else:  # 'Shared Room'
                    return 3
            else:
                return 0
        except:
            return 0

    def execute_select_query(self, query):
        # execute query
        query_results = self._db.execute(query).fetchall()
        # object mapping
        return self.map_result(query_results)

    def map_result(self, query_result):
        # Must be implemented by subclass
        raise NotImplementedError
