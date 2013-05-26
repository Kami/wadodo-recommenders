from __future__ import absolute_import

__all__ = [
    'FacebookUserInfoProvider'
]

import zope.interface
import facebook

from wadodo_algorithm.models.user_info_provider import IUserInfoProvider
from wadodo_algorithm.models.user_info import UserInfo
from wadodo_algorithm.utils.date import born_str_to_age


class FacebookUserInfoProvider(object):
    zope.interface.implements(IUserInfoProvider)

    name = 'Facebook'

    def __init__(self, access_token):
        self.access_token = access_token
        self._graph = facebook.GraphAPI(self.access_token)

    def get_user_info(self):
        profile = self._get_profile()
        name = profile['name']
        gender = profile['gender']
        age = born_str_to_age(profile['birthday'])
        ui = UserInfo(name=name, gender=gender, age=age)
        return ui

    def _get_profile(self):
        data = self._graph.get_object('me')
        return data
