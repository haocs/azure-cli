# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AutoscaleNotification(Model):
    """
    Autoscale notification.

    :param operation: Gets or sets the operation associated with the
     notification.
    :type operation: str
    :param email: Gets or sets the email notification.
    :type email: :class:`EmailNotification
     <insights.models.EmailNotification>`
    :param webhooks: Gets or sets the collection of webhook notifications.
    :type webhooks: list of :class:`WebhookNotification
     <insights.models.WebhookNotification>`
    """ 

    _attribute_map = {
        'operation': {'key': 'operation', 'type': 'str'},
        'email': {'key': 'email', 'type': 'EmailNotification'},
        'webhooks': {'key': 'webhooks', 'type': '[WebhookNotification]'},
    }

    def __init__(self, operation=None, email=None, webhooks=None):
        self.operation = operation
        self.email = email
        self.webhooks = webhooks
