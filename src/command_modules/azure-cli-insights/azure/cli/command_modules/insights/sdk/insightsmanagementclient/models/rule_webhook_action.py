# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .rule_action import RuleAction


class RuleWebhookAction(RuleAction):
    """
    Specifies the action to post to service when the rule condition is
    evaluated.

    :param odata.type: Polymorphic Discriminator
    :type odata.type: str
    :param service_uri: Gets or sets the service uri to Post the notitication.
    :type service_uri: str
    :param properties: Gets or sets the dictionary of custom properties to
     include with the post operation.
    :type properties: dict
    """ 

    _validation = {
        'odata.type': {'required': True},
    }

    _attribute_map = {
        'odata.type': {'key': 'odata.type', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(self, service_uri=None, properties=None):
        super(RuleWebhookAction, self).__init__()
        self.service_uri = service_uri
        self.properties = properties
        self.odata.type = 'Microsoft.Azure.Management.Insights.Models.RuleWebhookAction'
