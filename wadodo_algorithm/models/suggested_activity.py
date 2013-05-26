__all__ = [
    'SuggestedActivity'
]

import zope.interface


class ISuggestedActivity(zope.interface.Interface):
    """
    Represents activity suggested for a user.
    """
    activity = zope.interface.Attribute("""Suggested activity""")

    confidence = zope.interface.Attribute("""Confidence level between 0-100%
    (for absolute sorting)""")
    score = zope.interface.Attribute("""User matching score - used for
    relative sorting (e.g. activity with score 100 is a better match then
    activity with score 99)""")


class SuggestedActivity(object):
    zope.interface.implements(ISuggestedActivity)

    def __init__(self, activity, confidence=0, score=0):
        self.activity = activity
        self.confidence = confidence
        self.score = score
