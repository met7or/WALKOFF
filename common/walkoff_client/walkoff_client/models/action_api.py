# coding: utf-8

"""
    WALKOFF

    An active cyber defense development framework enabling orchestration capabilities to be written once and deployed across WALKOFF-enabled orchestration tools. https://nsacyber.github.io/WALKOFF/  # noqa: E501

    The version of the OpenAPI document: 0.9.1
    Contact: walkoff@nsa.gov
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ActionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'deprecated': 'bool',
        'description': 'str',
        'external_docs': 'list[ExternalDoc]',
        'name': 'str',
        'node_type': 'str',
        'parameters': 'list[ParameterApi]',
        'returns': 'ReturnApi'
    }

    attribute_map = {
        'deprecated': 'deprecated',
        'description': 'description',
        'external_docs': 'external_docs',
        'name': 'name',
        'node_type': 'node_type',
        'parameters': 'parameters',
        'returns': 'returns'
    }

    def __init__(self, deprecated=False, description=None, external_docs=None, name=None, node_type='ACTION', parameters=None, returns=None):  # noqa: E501
        """ActionApi - a model defined in OpenAPI"""  # noqa: E501

        self._deprecated = None
        self._description = None
        self._external_docs = None
        self._name = None
        self._node_type = None
        self._parameters = None
        self._returns = None
        self.discriminator = None

        if deprecated is not None:
            self.deprecated = deprecated
        if description is not None:
            self.description = description
        if external_docs is not None:
            self.external_docs = external_docs
        self.name = name
        if node_type is not None:
            self.node_type = node_type
        if parameters is not None:
            self.parameters = parameters
        if returns is not None:
            self.returns = returns

    @property
    def deprecated(self):
        """Gets the deprecated of this ActionApi.  # noqa: E501

        Is this action deprecated?  # noqa: E501

        :return: The deprecated of this ActionApi.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this ActionApi.

        Is this action deprecated?  # noqa: E501

        :param deprecated: The deprecated of this ActionApi.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def description(self):
        """Gets the description of this ActionApi.  # noqa: E501

        A longer description of the operation  # noqa: E501

        :return: The description of this ActionApi.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ActionApi.

        A longer description of the operation  # noqa: E501

        :param description: The description of this ActionApi.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def external_docs(self):
        """Gets the external_docs of this ActionApi.  # noqa: E501


        :return: The external_docs of this ActionApi.  # noqa: E501
        :rtype: list[ExternalDoc]
        """
        return self._external_docs

    @external_docs.setter
    def external_docs(self, external_docs):
        """Sets the external_docs of this ActionApi.


        :param external_docs: The external_docs of this ActionApi.  # noqa: E501
        :type: list[ExternalDoc]
        """

        self._external_docs = external_docs

    @property
    def name(self):
        """Gets the name of this ActionApi.  # noqa: E501

        Unique name of the action  # noqa: E501

        :return: The name of this ActionApi.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActionApi.

        Unique name of the action  # noqa: E501

        :param name: The name of this ActionApi.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def node_type(self):
        """Gets the node_type of this ActionApi.  # noqa: E501

        The node type this action represents  # noqa: E501

        :return: The node_type of this ActionApi.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ActionApi.

        The node type this action represents  # noqa: E501

        :param node_type: The node_type of this ActionApi.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTION", "CONDITION", "TRANSFORM", "TRIGGER"]  # noqa: E501
        if node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def parameters(self):
        """Gets the parameters of this ActionApi.  # noqa: E501

        The parameters needed by this action  # noqa: E501

        :return: The parameters of this ActionApi.  # noqa: E501
        :rtype: list[ParameterApi]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ActionApi.

        The parameters needed by this action  # noqa: E501

        :param parameters: The parameters of this ActionApi.  # noqa: E501
        :type: list[ParameterApi]
        """

        self._parameters = parameters

    @property
    def returns(self):
        """Gets the returns of this ActionApi.  # noqa: E501


        :return: The returns of this ActionApi.  # noqa: E501
        :rtype: ReturnApi
        """
        return self._returns

    @returns.setter
    def returns(self, returns):
        """Sets the returns of this ActionApi.


        :param returns: The returns of this ActionApi.  # noqa: E501
        :type: ReturnApi
        """

        self._returns = returns

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActionApi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
