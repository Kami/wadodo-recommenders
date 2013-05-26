__all__ = [
    'UserInfo'
]

import zope.interface

from wadodo_algorithm.utils.misc import ClassRepresentationMixin


class IUserInfo(zope.interface.Interface):
    """
    Contains facts and information about the user preferences / likes.
    """

    name = zope.interface.Attribute("""User first and last name""")
    gender = zope.interface.Attribute("""""")
    age = zope.interface.Attribute("""""")


class UserInfo(ClassRepresentationMixin):
    zope.interface.implements(IUserInfo)

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
