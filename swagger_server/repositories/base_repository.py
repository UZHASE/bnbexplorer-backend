import os
import sqlite3


class Repository(object):

    def __init__(self):
        self.__connection = sqlite3.connect(str(os.environ.get('DB_PATH', 'database/bnbexplorer.sqlite')))
        # TODO: Should we keep this? Allows to get query results as dicts.
        # See https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
        self.__connection.row_factory = sqlite3.Row
        self._db = self.__connection.cursor()
