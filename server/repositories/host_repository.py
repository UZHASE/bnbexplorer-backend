from server.repositories.base_repository import Repository
from server.models.host import Host as Host_Model
from pypika import Query


class Host(Repository):

    def get_by_id(self, host_id):
        query = self.build_get_by_id_query(host_id)

        return self.execute_select_query(query)

    def build_get_by_id_query(self, host_id):

        return Query\
            .from_(self.hosts)\
            .select(self.hosts.id, self.hosts.name, self.hosts.num_of_listings.as_('numOfListings'))\
            .where(self.hosts.id == host_id)\
            .get_sql()

    def map_result(self, query_results):
        return [Host_Model.from_dict(dict(row)) for row in query_results]
