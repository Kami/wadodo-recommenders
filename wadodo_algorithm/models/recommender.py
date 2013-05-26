import zope.interface

__all__ = [
    'IRecommender'
]


class IRecommender(zope.interface.Interface):
    name = zope.interface.Attribute("""Recommender name""")

    def get_recommended_activities(self, activities, user_info):
        """
        From a list of provided activies return ones which are a good match for
        the provided user info.
        """
