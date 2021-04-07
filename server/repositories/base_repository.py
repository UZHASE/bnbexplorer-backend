import os
import sqlite3


class Repository(object):
    # set row limit (temporary)
    ROW_LIMIT = 1000

    def __init__(self):
        self.__connection = sqlite3.connect(str(os.environ.get('DB_PATH', 'database/bnbexplorer.sqlite')))
        self.__connection.row_factory = sqlite3.Row
        self._db = self.__connection.cursor()