# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EventData(Model):
    """
    The Azure event log entries are of type EventData

    :param authorization: Gets or sets the authorization.This is the
     authorization used by the user who has performed the operation that led
     to this event.
    :type authorization: :class:`SenderAuthorization
     <insights.models.SenderAuthorization>`
    :param channels: Gets or sets the event channels.The regular event logs,
     that you see in the Azure Management Portals, flow through the
     'Operation' channel. Possible values include: 'Admin', 'Operation',
     'Debug', 'Analytics'
    :type channels: str or :class:`EventChannels
     <insightsclient.models.EventChannels>`
    :param claims: Gets or sets the claims
    :type claims: dict
    :param caller: Gets or sets the caller
    :type caller: str
    :param description: Gets or sets the description of the event.
    :type description: str
    :param id: Gets or sets the Id
    :type id: str
    :param event_data_id: Gets or sets the event data Id.This is a unique
     identifier for an event.
    :type event_data_id: str
    :param correlation_id: Gets or sets the correlation Id.The correlation Id
     is shared among the events that belong to the same deployment.
    :type correlation_id: str
    :param event_name: Gets or sets the event name.This value should not be
     confused with OperationName.For practical purposes, OperationName might
     be more appealing to end users.
    :type event_name: :class:`LocalizableString
     <insights.models.LocalizableString>`
    :param category: Gets or sets the event category.
    :type category: :class:`LocalizableString
     <insights.models.LocalizableString>`
    :param http_request: Gets or sets the HTTP request info.The client IP
     address of the user who initiated the event is captured as part of the
     HTTP request info.
    :type http_request: :class:`HttpRequestInfo
     <insights.models.HttpRequestInfo>`
    :param level: Gets or sets the event level. Possible values include:
     'Critical', 'Error', 'Warning', 'Informational', 'Verbose'
    :type level: str or :class:`EventLevel <insightsclient.models.EventLevel>`
    :param resource_group_name: Gets or sets the resource group name.
    :type resource_group_name: str
    :param resource_provider_name: Gets or sets the resource provider name.
    :type resource_provider_name: :class:`LocalizableString
     <insights.models.LocalizableString>`
    :param resource_id: Gets or sets the resource uri
    :type resource_id: str
    :param resource_type: Gets or sets the resource type
    :type resource_type: :class:`LocalizableString
     <insights.models.LocalizableString>`
    :param operation_id: Gets or sets the operation idThis value should not
     be confused with EventName.
    :type operation_id: str
    :param operation_name: Gets or sets the operation name.
    :type operation_name: :class:`LocalizableString
     <insights.models.LocalizableString>`
    :param properties: Gets or sets the property bag
    :type properties: dict
    :param status: Gets or sets the event status.Some typical values are:
     Started, Succeeded, Failed
    :type status: :class:`LocalizableString
     <insights.models.LocalizableString>`
    :param sub_status: Gets or sets the event sub status.Most of the time,
     when included, this captures the HTTP status code.
    :type sub_status: :class:`LocalizableString
     <insights.models.LocalizableString>`
    :param event_timestamp: Gets or sets the occurrence time of event
    :type event_timestamp: datetime
    :param submission_timestamp: Gets or sets the event submission time.This
     value should not be confused eventTimestamp. As there might be a delay
     between the occurence time of the event, and the time that the event is
     submitted to the Azure logging infrastructure.
    :type submission_timestamp: datetime
    :param subscription_id: Gets or sets the Azure subscription Id
    :type subscription_id: str
    :param tenant_id: Gets or sets the Azure tenant Id
    :type tenant_id: str
    """ 

    _validation = {
        'channels': {'required': True},
        'level': {'required': True},
        'event_timestamp': {'required': True},
        'submission_timestamp': {'required': True},
    }

    _attribute_map = {
        'authorization': {'key': 'authorization', 'type': 'SenderAuthorization'},
        'channels': {'key': 'channels', 'type': 'EventChannels'},
        'claims': {'key': 'claims', 'type': '{str}'},
        'caller': {'key': 'caller', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'event_data_id': {'key': 'eventDataId', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'event_name': {'key': 'eventName', 'type': 'LocalizableString'},
        'category': {'key': 'category', 'type': 'LocalizableString'},
        'http_request': {'key': 'httpRequest', 'type': 'HttpRequestInfo'},
        'level': {'key': 'level', 'type': 'EventLevel'},
        'resource_group_name': {'key': 'resourceGroupName', 'type': 'str'},
        'resource_provider_name': {'key': 'resourceProviderName', 'type': 'LocalizableString'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'resource_type': {'key': 'resourceType', 'type': 'LocalizableString'},
        'operation_id': {'key': 'operationId', 'type': 'str'},
        'operation_name': {'key': 'operationName', 'type': 'LocalizableString'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'status': {'key': 'status', 'type': 'LocalizableString'},
        'sub_status': {'key': 'subStatus', 'type': 'LocalizableString'},
        'event_timestamp': {'key': 'eventTimestamp', 'type': 'iso-8601'},
        'submission_timestamp': {'key': 'submissionTimestamp', 'type': 'iso-8601'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, channels, level, event_timestamp, submission_timestamp, authorization=None, claims=None, caller=None, description=None, id=None, event_data_id=None, correlation_id=None, event_name=None, category=None, http_request=None, resource_group_name=None, resource_provider_name=None, resource_id=None, resource_type=None, operation_id=None, operation_name=None, properties=None, status=None, sub_status=None, subscription_id=None, tenant_id=None):
        self.authorization = authorization
        self.channels = channels
        self.claims = claims
        self.caller = caller
        self.description = description
        self.id = id
        self.event_data_id = event_data_id
        self.correlation_id = correlation_id
        self.event_name = event_name
        self.category = category
        self.http_request = http_request
        self.level = level
        self.resource_group_name = resource_group_name
        self.resource_provider_name = resource_provider_name
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.operation_id = operation_id
        self.operation_name = operation_name
        self.properties = properties
        self.status = status
        self.sub_status = sub_status
        self.event_timestamp = event_timestamp
        self.submission_timestamp = submission_timestamp
        self.subscription_id = subscription_id
        self.tenant_id = tenant_id
