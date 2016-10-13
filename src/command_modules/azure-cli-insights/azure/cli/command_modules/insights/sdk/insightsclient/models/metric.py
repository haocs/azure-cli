# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Metric(Model):
    """A set of metric values in a time range.

    :param name: the name and the display name of the metric.
    :type name: :class:`LocalizableString
     <azure.insights.models.LocalizableString>`
    :param unit: the unit of the metric. Possible values include: 'Count',
     'Bytes', 'Seconds', 'CountPerSecond', 'BytesPerSecond', 'Percent',
     'MilliSeconds'
    :type unit: str or :class:`Unit <azure.insights.models.Unit>`
    :param data: Array of data points representing the metric values.
    :type data: list of :class:`MetricValue
     <azure.insights.models.MetricValue>`
    """ 

    _validation = {
        'name': {'required': True},
        'unit': {'required': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'unit': {'key': 'unit', 'type': 'Unit'},
        'data': {'key': 'data', 'type': '[MetricValue]'},
    }

    def __init__(self, name, unit, data):
        self.name = name
        self.unit = unit
        self.data = data