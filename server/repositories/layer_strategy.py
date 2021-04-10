import abc

from pypika import Table, Query
from server.models.layer import Layer as Layer_Model
from server.models.layer import LayerEntry as LayerEntry_Model
from server.models.layer_type import LayerType


class LayerStrategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported layers. Context
    uses this interface to call the layer defined by a
    LayerStrategy.
    """

    @abc.abstractmethod
    def build_get_all_query(self):
        pass

    @abc.abstractmethod
    def map_result(self, query_results):
        pass


class HealthLayerStrategy(LayerStrategy):
    """
    Implement health layer using the Strategy interface.
    """

    def build_get_all_query(self):
        # table
        rat_sightings = Table('rat_sightings')
        # query building
        query = Query \
            .from_(rat_sightings) \
            .select(rat_sightings.latitude, rat_sightings.longitude)

        return query.get_sql()

    def map_result(self, query_results):
        # object mapping
        layer = Layer_Model(type=LayerType.HEALTH.value)
        result = []
        for row in query_results:
            row = dict(row)
            listing = LayerEntry_Model.from_dict(row)
            result.append(listing)
        layer.entries = result
        return layer


class CrimeLayerStrategy(LayerStrategy):
    """
    Implement the crime layer using the Strategy interface.
    """

    def build_get_all_query(self):
        # table
        nypd_incidents = Table('nypd_incidents')
        # query building
        query = Query \
            .from_(nypd_incidents) \
            .select(nypd_incidents.latitude, nypd_incidents.longitude)

        return query.get_sql()

    def map_result(self, query_results):
        # object mapping
        layer = Layer_Model(type=LayerType.CRIME.value)
        result = []
        for row in query_results:
            row = dict(row)
            listing = LayerEntry_Model.from_dict(row)
            result.append(listing)
        layer.entries = result
        return layer
