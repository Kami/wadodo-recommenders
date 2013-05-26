import zope.interface

from wadodo_algorithm.models.matcher import IMatcher

__all__ = [
    'SimpleCategoryMatcher'
]


class SimpleCategoryMatcher(object):
    zope.interface.implements(IMatcher)

    def _get_likes_relative_importance(self, likes):
        relative_importance = {}

        total_likes = 0
        for like in likes:
            category = like.category

            if category not in relative_importance:
                relative_importance[category] = {'count': 0,
                                                 'relative_importance': 0}

            relative_importance[category]['count'] += 1
            total_likes += 1

        for like in likes:
            category = like.category
            item = relative_importance[category]
            count = item['count']
            item['relative_importance'] = float(count) / total_likes

        return relative_importance

    def get_matched_activities(self, activities, user_info):
        relative_importance = \
            self._get_likes_relative_importance(user_info.likes)
