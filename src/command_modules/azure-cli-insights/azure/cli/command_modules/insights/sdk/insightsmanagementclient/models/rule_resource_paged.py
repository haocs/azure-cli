# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class RuleResourcePaged(Paged):
    """
    A paging container for iterating over a list of RuleResource object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RuleResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(RuleResourcePaged, self).__init__(*args, **kwargs)
