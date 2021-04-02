from swagger_server.repositories.base_repository import Repository
from swagger_server.models.listing import Listing as Listing_Model


class Listing(Repository):

    def get_all(self):
        self._db.execute('SELECT * FROM listings LIMIT 200')

        # TODO: We should serialize query results to models like this:
        #  [Listing_Model.from_dict(dict(row)) for row in self._db.fetchall()]
        #  Currently, this is not working as models and DB schema must match.
        return [dict(row) for row in self._db.fetchall()]
