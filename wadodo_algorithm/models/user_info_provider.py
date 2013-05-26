__all__ = [
    'IUserInfoProvider'
]

import zope.interface


class IUserInfoProvider(zope.interface.Interface):
    """
    Class which provides information about some user. Example providers include
    Facebook, Google, Foursquare, etc.
    """
    title = zope.interface.Attribute("""Provider name""")
    access_token = zope.interface.Attribute("""Token used to access the user data""")

    def get_user_info(self):
        """
        Return UserInfo object.
        """
