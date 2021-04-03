# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LayerEntry(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, latitude: float=None, longitude: float=None):  # noqa: E501
        """LayerEntry - a model defined in Swagger

        :param id: The id of this LayerEntry.  # noqa: E501
        :type id: int
        :param latitude: The latitude of this LayerEntry.  # noqa: E501
        :type latitude: float
        :param longitude: The longitude of this LayerEntry.  # noqa: E501
        :type longitude: float
        """
        self.swagger_types = {
            'id': int,
            'latitude': float,
            'longitude': float
        }

        self.attribute_map = {
            'id': 'id',
            'latitude': 'latitude',
            'longitude': 'longitude'
        }
        self._id = id
        self._latitude = latitude
        self._longitude = longitude

    @classmethod
    def from_dict(cls, dikt) -> 'LayerEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LayerEntry of this LayerEntry.  # noqa: E501
        :rtype: LayerEntry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this LayerEntry.


        :return: The id of this LayerEntry.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this LayerEntry.


        :param id: The id of this LayerEntry.
        :type id: int
        """

        self._id = id

    @property
    def latitude(self) -> float:
        """Gets the latitude of this LayerEntry.


        :return: The latitude of this LayerEntry.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this LayerEntry.


        :param latitude: The latitude of this LayerEntry.
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Gets the longitude of this LayerEntry.


        :return: The longitude of this LayerEntry.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this LayerEntry.


        :param longitude: The longitude of this LayerEntry.
        :type longitude: float
        """

        self._longitude = longitude