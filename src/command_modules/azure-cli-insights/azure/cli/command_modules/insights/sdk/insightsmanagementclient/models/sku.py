# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Sku(Model):
    """
    Represents a sku.

    :param name: Gets or sets the unique name of the sku e.g. 'Free_A0'.
    :type name: str
    :param tier: Gets or sets the tier of the sku e.g. 'free'.
    :type tier: str
    :param size: Gets or sets the size of the sku e.g. 'A0'.
    :type size: str
    :param family: Gets or sets the family of the sku e.g. 'A'.
    :type family: str
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
    }

    def __init__(self, name=None, tier=None, size=None, family=None):
        self.name = name
        self.tier = tier
        self.size = size
        self.family = family
