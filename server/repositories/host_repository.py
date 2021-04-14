from server.repositories.base_repository import Repository
from server.models.host import Host as Host_Model
from pypika import Query, Table


class Host(Repository):

    def get_by_id(self, host_id):
        query = self.build_get_by_id_query(host_id)

        return self.execute_select_query(query)

    def build_get_by_id_query(self, host_id):
        hosts = Table('hosts')

        return Query\
            .from_(hosts)\
            .select(hosts.id, hosts.name, hosts.num_of_listings.as_('numOfListings'))\
            .where(hosts.id == host_id)\
            .get_sql()

    def map_result(self, query_results):
        return [Host_Model.from_dict(dict(row)) for row in query_results]
