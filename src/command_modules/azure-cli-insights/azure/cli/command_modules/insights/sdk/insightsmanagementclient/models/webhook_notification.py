# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WebhookNotification(Model):
    """
    Webhook notification.

    :param service_uri: Gets or sets the service address to receive the
     notification.
    :type service_uri: str
    :param properties: Gets or sets a property bag of settings.
    :type properties: dict
    """ 

    _attribute_map = {
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(self, service_uri=None, properties=None):
        self.service_uri = service_uri
        self.properties = properties
