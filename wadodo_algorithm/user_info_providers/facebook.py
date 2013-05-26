from __future__ import absolute_import

__all__ = [
    'FacebookUserInfoProvider'
]

import zope.interface
import facebook

from wadodo_algorithm.models.user_info_provider import IUserInfoProvider
from wadodo_algorithm.models.user_info import UserInfo
from wadodo_algorithm.models.like import Like
from wadodo_algorithm.utils.date import born_str_to_age


class FacebookUserInfoProvider(object):

    """
    UserInfoProvider which uses Facebook's Graph API as a primary data source.

    https://developers.facebook.com/docs/reference/api/user/
    """
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

        likes = self._get_and_format_likes()

        ui = UserInfo(name=name, gender=gender, age=age, likes=likes)
        return ui

    def _get_and_format_likes(self):
        result = []
        items = self._get_likes()

        for item in items:
            description = item.get('description', None)
            like = Like(title=item['name'], category=item['category'],
                        description=description)
            result.append(like)

        return result

    def _get_profile(self):
        data = self._graph.get_object('me')
        return data

    def _get_likes(self):
        fields = ['name', 'category', 'description']
        data = self._graph.get_object('me/likes', fields=fields)['data']
        return data
