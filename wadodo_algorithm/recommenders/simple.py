import zope.interface

from wadodo_algorithm.models.recommender import IRecommender

__all__ = [
    'SimpleCategoryRecommender'
]

# Maps Wadodo category to Facebook category
WADODO_TO_FACEBOOK_CATEGORY_MAP = {
    'Food': [],
    'Music': ['Music'],
    'Theatre': [],
    'Heritage & Buildings': [],
    'Nature': [],
    'Shopping': [],
    'Adrenaline': [],
    'Relaxation & Spa': ['Health/beauty'],
    'Automotive': [],
    'Art': [],
    'Sport': ['Sport', 'Athlete'],
    'Religion': [],
    'Casinos': [],
    'Adult': [],
    'Nightlife': ['Clubs']
}

# Reverse of WADODO_TO_FACEBOOK_CATEGORY_MAP
FACEBOOK_TO_WADODO_CATEGORY_MAP = {}

for wadodo_category, facebook_categories in WADODO_TO_FACEBOOK_CATEGORY_MAP:
    for facebook_category in facebook_categories:
        FACEBOOK_TO_WADODO_CATEGORY_MAP[facebook_category] = wadodo_category


class SimpleCategoryRecommender(object):
    """
    A recommender which finds matching activities based on the relative
    importance from categories which are parsed from user's likes.
    """

    zope.interface.implements(IRecommender)

    def __init__(self, threshold):
        """
        @param threshold: Score threshold for the activity to be included in
                          the resulting set.
        @type threshold: C{float}
        """
        self._threshold = float(threshold)

    def get_recommended_activities(self, activities, user_info):
        recommended_activities = []
        relative_importance = \
            self._get_likes_relative_importance(user_info.likes)

        for activity in activities:
            score = self._calculate_activity_matching_score(activity=activity,
                    relative_importance=relative_importance)

            if score < self._threshold:
                # Score is too low to include it
                continue

    def _calculate_activity_matching_score(self, activity,
                                           relative_importance):
        score = 0

        for category in activity.categories:
            if not category in relative_importance:
                continue

            category_ri = relative_importance[category]
            score += category_ri

        return score

    def _get_likes_relative_importance(self, likes):
        """
        Build category relative importance table.

        Return a dictionary where a key is a Wadodo category name and value
        is dictionary with keys 'count' and 'relative_importance'.
        """
        relative_importance = {}

        total_likes = 0
        for like in likes:
            facebook_category = like.category
            wadodo_category = \
                FACEBOOK_TO_WADODO_CATEGORY_MAP.get(facebook_category)

            if not wadodo_category:
                # Doesn't map to wadodo category, skip it.
                continue

            if wadodo_category not in relative_importance:
                relative_importance[wadodo_category] = {}
                relative_importance[wadodo_category]['count'] = 0
                relative_importance[wadodo_category]['relative_importance'] = 0

            relative_importance[wadodo_category]['count'] += 1
            total_likes += 1

        for category in relative_importance.keys():
            item = relative_importance[category]
            count = item['count']
            item['relative_importance'] = float(count) / total_likes

        return relative_importance
