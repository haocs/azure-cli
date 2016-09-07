# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RetentionPolicy(Model):
    """
    Part of MultiTenantDiagnosticSettings. Child of MetricSettings. Specifies
    the retention policy for the specific metric.

    :param enabled: Gets or sets a value indicating whether the retention
     policy is enabled.
    :type enabled: bool
    :param days: Gets or sets the number of days for the retention.
    :type days: int
    """ 

    _validation = {
        'enabled': {'required': True},
        'days': {'required': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'days': {'key': 'days', 'type': 'int'},
    }

    def __init__(self, enabled, days):
        self.enabled = enabled
        self.days = days
