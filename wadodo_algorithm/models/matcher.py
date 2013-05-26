import zope.interface

__all__ = [
    'IMatcher'
]


class IMatcher(zope.interface.Interface):
    name = zope.interface.Attribute("""Matcher name""")

    def get_matched_activities(self, activities, user_info):
        """
        From a list of provided activies return ones which are a good match for
        the provided user info.
        """
