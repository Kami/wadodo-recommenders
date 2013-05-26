__all__ = [
    'UserInfo'
]

import zope.interface

from wadodo_algorithm.utils.misc import ClassRepresentationMixin


class IUserInfo(zope.interface.Interface):

    """
    Contains facts and information about the user preferences / likes.
    """

    name = zope.interface.Attribute("""First and last name""")
    gender = zope.interface.Attribute("""Gender""")
    age = zope.interface.Attribute("""Age (in years)""")

    likes = zope.interface.Attribute(
        """A list of C{Like} objects for this user""")


class UserInfo(ClassRepresentationMixin):
    zope.interface.implements(IUserInfo)

    def __init__(self, name, gender, age, likes=None):
        self.name = name
        self.gender = gender
        self.age = age
        self.likes = likes or {}
