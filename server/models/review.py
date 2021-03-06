# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server.utils import util


class Review(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, listing_id: int=None, text: str=None):  # noqa: E501
        """Review - a model defined in Swagger

        :param id: The id of this Review.  # noqa: E501
        :type id: int
        :param listing_id: The listing_id of this Review.  # noqa: E501
        :type listing_id: int
        :param text: The text of this Review.  # noqa: E501
        :type text: str
        """
        self.swagger_types = {
            'id': int,
            'listing_id': int,
            'text': str
        }

        self.attribute_map = {
            'id': 'id',
            'listing_id': 'listingId',
            'text': 'text'
        }
        self._id = id
        self._listing_id = listing_id
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'Review':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Review of this Review.  # noqa: E501
        :rtype: Review
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Review.


        :return: The id of this Review.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Review.


        :param id: The id of this Review.
        :type id: int
        """

        self._id = id

    @property
    def listing_id(self) -> int:
        """Gets the listing_id of this Review.


        :return: The listing_id of this Review.
        :rtype: int
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id: int):
        """Sets the listing_id of this Review.


        :param listing_id: The listing_id of this Review.
        :type listing_id: int
        """

        self._listing_id = listing_id

    @property
    def text(self) -> str:
        """Gets the text of this Review.


        :return: The text of this Review.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this Review.


        :param text: The text of this Review.
        :type text: str
        """

        self._text = text
