from __future__ import absolute_import

__all__ = [
    'FacebookUserInfoProvider'
]

from collections import defaultdict

import zope.interface
import facebook
from nltk.stem.wordnet import WordNetLemmatizer

from wadodo_algorithm.models.user_info_provider import IUserInfoProvider
from wadodo_algorithm.models.user_info import UserInfo
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
        #self._lemmatizer = WordNetLemmatizer()

        # Warm it up (load cropus data)
        #self._lemmatizer.lemmatize('')

    def get_likes(self):
        result = []
        likes = self._get_likes()

        for item in likes:
            category = item['category']
            result.append(category)

        return result

    def get_user_info(self):
        profile = self._get_profile()
        name = profile['name']
        gender = profile['gender']
        age = born_str_to_age(profile['birthday'])
        likes = self._get_likes()

        ui = UserInfo(name=name, gender=gender, age=age, likes=likes)
        return ui

    def _get_profile(self):
        data = self._graph.get_object('me')
        return data

    def _get_likes(self):
        data = self._graph.get_object('me/likes')['data']
        return data
