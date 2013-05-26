__all__ = [
    'Activity'
]

import zope.interface


class IActivity(zope.interface.Interface):
    """
    Represents an acitivity.
    """

    title = zope.interface.Attribute("""""")
    categories = zope.interface.Attribute("""""")
    age_groups = zope.interface.Attribute("""""")
    gender_groups = zope.interface.Attribute("""""")
    social_groups = zope.interface.Attribute("""""")
    price_range = zope.interface.Attribute("""""")
    time_needed = zope.interface.Attribute("""""")
    location = zope.interface.Attribute("""""")

    # Rating, reviews
    score = zope.interface.Attribute("""""")
    ratings = zope.interface.Attribute("""""")
    reviews = zope.interface.Attribute("""""")


class Activity(object):
    zope.interface.implements(IActivity)

    def __init__(self, title, categories, age_groups, gender_groups,
                 price_range, time_needed, location, score=0, ratings=None,
                 reviews=None):
        self.title = title
        self.categories = categories
        self.age_groups = age_groups
        self.gender_groups = gender_groups
        self.price_range = price_range
        self.time_needed = time_needed
        self.location = location
        self.score = score
        self.ratings = ratings or []
        self.ratings = reviews or []
