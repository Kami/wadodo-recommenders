import zope.interface

__all__ = [
    'Like'
]


class ILike(zope.interface.Interface):
    """
    Represents an entity user has liked.
    """
    title = zope.interface.Attribute("""""")
    category = zope.interface.Attribute("""""")
    description = zope.interface.Attribute("""""")


class Like(object):
    zope.interface.implements(ILike)

    def __init__(self, title, category=None, description=None):
        self.title = title
        self.category = category
        self.description = description
