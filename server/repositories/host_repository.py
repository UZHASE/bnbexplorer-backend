from server.repositories.base_repository import Repository
from server.models.host import Host as Host_Model


class Host(Repository):

    def get_by_id(self, host_id):
        query_result = self._db.execute('''
            SELECT id, name, num_of_listings numOfListings 
            FROM hosts 
            WHERE id=?
        ''', (host_id,)).fetchone()

        return Host_Model.from_dict(dict(query_result))