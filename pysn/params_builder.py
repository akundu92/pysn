
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Robert Wikman <rbw@vault13.org>
import six

from .query_builder import QueryBuilder

from .exceptions import InvalidUsage


class ParamsBuilder(object):
    """Provides an interface for setting / getting common ServiceNow sysparms."""

    def __init__(self):
        self._custom_params = {}

        self._sysparms = {
            'sysparm_query': '',
            'sysparm_limit': 10000,
            'sysparm_offset': None,
            'sysparm_display_value': False,
            'sysparm_suppress_pagination_header': False,
            'sysparm_exclude_reference_link': False,
            'sysparm_view': '',
            'sysparm_fields': []
        }

    @staticmethod
    def stringify_query(query):
        """Stringifies the query (dict or QueryBuilder) into a ServiceNow-compatible format

        :return:
            - ServiceNow-compatible string-type query
        """

        if isinstance(query, QueryBuilder):
            # Get string-representation of the passed :class:`pysnow.QueryBuilder` object
            return str(query)
        elif isinstance(query, dict):
            # Dict-type query
            return '^'.join(['%s=%s' % (k, v) for k, v in six.iteritems(query)])
        elif isinstance(query, six.string_types):
            # Regular string-type query
            return query
        else:
            raise InvalidUsage('Query must be of type string, dict or a QueryBuilder object')

    def add_custom(self, params):
        """Adds new custom parameter after making sure it's of type dict.

        :param params: Dictionary containing one or more parameters
        """

        if isinstance(params, dict) is False:
            raise InvalidUsage("custom parameters must be of type `dict`")

        self._custom_params.update(params)

    @property
    def custom_params(self):
        """Returns a dictionary of added custom parameters"""
        return self._custom_params

    @property
    def display_value(self):
        """Maps to `sysparm_display_value`"""
        return self._sysparms['sysparm_display_value']

    @display_value.setter
    def display_value(self, value):
        """Sets `sysparm_display_value`

        :param value:  Bool or 'all'
        """

        if not (isinstance(value, bool) or value == 'all'):
            raise InvalidUsage("Display value can be of type bool or value 'all'")

        self._sysparms['sysparm_display_value'] = value

    @property
    def query(self):
        """Maps to `sysparm_query`"""
        return self._sysparms['sysparm_query']

    @query.setter
    def query(self, query):
        """Validates, stringifies and sets `sysparm_query`

        :param query: String, dict or QueryBuilder
        """

        self._sysparms['sysparm_query'] = self.stringify_query(query)

    @property
    def limit(self):
        """Maps to `sysparm_limit`"""
        return self._sysparms['sysparm_limit']

    @limit.setter
    def limit(self, limit):
        """Sets `sysparm_limit`

        :param limit: Size limit (int)
        """

        if not isinstance(limit, int) or isinstance(limit, bool):
            raise InvalidUsage("limit size must be of type integer")

        self._sysparms['sysparm_limit'] = limit

    @property
    def offset(self):
        """Maps to `sysparm_offset`"""
        return self._sysparms['sysparm_offset']

    @offset.setter
    def offset(self, offset):
        """Sets `sysparm_offset`, usually used to accomplish pagination

        :param offset: Number of records to skip before fetching records
        :raise:
            :InvalidUsage: if offset is of an unexpected type
        """

        if not isinstance(offset, int) or isinstance(offset, bool):
            raise InvalidUsage('Offset must be an integer')

        self._sysparms['sysparm_offset'] = offset

    @property
    def fields(self):
        """Maps to `sysparm_fields`"""
        return self._sysparms['sysparm_fields']

    @fields.setter
    def fields(self, fields):
        """Sets `sysparm_fields` after joining the given list of `fields`

        :param fields: List of fields to include in the response
        :raise:
            :InvalidUsage: if fields is of an unexpected type
        """

        if not isinstance(fields, list):
            raise InvalidUsage('fields must be of type `list`')

        self._sysparms['sysparm_fields'] = ",".join(fields)

    @property
    def exclude_reference_link(self):
        """Maps to `sysparm_exclude_reference_link`"""
        return self._sysparms['sysparm_exclude_reference_link']

    @exclude_reference_link.setter
    def exclude_reference_link(self, exclude):
        """Sets `sysparm_exclude_reference_link` to a bool value

        :param exclude: bool
        """
        if not isinstance(exclude, bool):
            raise InvalidUsage('exclude_reference_link must be of type bool')

        self._sysparms['sysparm_exclude_reference_link'] = exclude

    @property
    def suppress_pagination_header(self):
        """Maps to `sysparm_suppress_pagination_header`"""
        return self._sysparms['sysparm_suppress_pagination_header']

    @suppress_pagination_header.setter
    def suppress_pagination_header(self, suppress):
        """Enables or disables pagination header by setting `sysparm_suppress_pagination_header`

        :param suppress: bool
        """
        if not isinstance(suppress, bool):
            raise InvalidUsage('suppress_pagination_header must be of type bool')

        self._sysparms['sysparm_suppress_pagination_header'] = suppress

    def aggregate_api_as_dict(self):
        raise  NotImplementedError


    def as_dict(self):
        """Constructs query params compatible with :class:`requests.Request`

        :return:
            - Dictionary containing query parameters
        """

        sysparms = self._sysparms
        sysparms.update(self._custom_params)

        return sysparms


class ParamsBuilderAggregate():
    def __init__(self):
       self.pb = ParamsBuilder()
       # self.pb._custom_params={}
       self.pb._sysparms = {
           'sysparm_query': '',
           'sysparm_avg_fields':None,
           'sysparm_count':False,
           'sysparm_min_fields':None,
           'sysparm_max_fields':None,
           'sysparm_sum_fields':None,
           'sysparm_group_by':None,
           'sysparm_order_by':None,
           'sysparm_having':None,
           'sysparm_display_value':False,
           'sysparm_query_category':None,
       }

    def add_custom(self, params):
        self.pb.add_custom(params)



    @property
    def query(self):
        """Maps to `sysparm_query`"""
        return self.pb.query

    @property
    def avg_fields(self):
        return self.pb._sysparms['sysparm_avg_fields']

    @avg_fields.setter
    def avg_fields(self,avg_fields):
        self.pb._sysparms['sysparm_avg_fields']=avg_fields


    @property
    def count(self):
        return self.pb._sysparms['sysparm_count']

    @count.setter
    def count(self,setter):
        self.pb._sysparms['sysparm_count']=setter

    @property
    def min_fields(self):
        return self.pb._sysparms['sysparm_min_fields']

    @min_fields.setter
    def min_fields(self,min_fields):
        self.pb._sysparms['sysparm_min_fields']=min_fields

    @property
    def max_fields(self):
        return self.pb._sysparms['sysparm_max_fields']

    @max_fields.setter
    def max_fields(self,max_fields):
        self.pb._sysparms['sysparm_max_fields']=max_fields

    @property
    def sum_fields(self):
        return self.pb._sysparms['sysparm_sum_fields']

    @sum_fields.setter
    def sum_fields(self,sum_fields):
        self.pb._sysparms['sysparm_sum_fields']=sum_fields

    @property
    def group_by(self):
        return self.pb._sysparms['sysparm_group_by']

    @group_by.setter
    def group_by(self,group_by):
        self.pb._sysparms['sysparm_group_by']=group_by

    @property
    def order_by(self):
        return self.pb._sysparms['sysparm_order_by']

    @order_by.setter
    def order_by(self,order_by):
        self.pb._sysparms['sysparm_order_by']=order_by

    @property
    def having(self):
        return self.pb._sysparms['sysparm_having']

    @having.setter
    def having(self,having):
        self.pb._sysparms['sysparm_having']=having

    @property
    def display_values(self):
        return self.pb._sysparms['sysparm_display_value']

    @display_values.setter
    def display_values(self,display_values):
        self.pb._sysparms['sysparm_display_value']=display_values

    @property
    def query_category(self):
        return self.pb._sysparms['sysparm_query_category']

    @query_category.setter
    def query_category(self,query_category):
        self.pb._sysparms['sysparm_query_category']=query_category

    @query.setter
    def query(self, query):
        """Validates, stringifies and sets `sysparm_query`

        :param query: String, dict or QueryBuilder
        """

        self.pb._sysparms['sysparm_query'] = ParamsBuilder.stringify_query(query)




    def as_dict(self):

        return self.pb.as_dict()








