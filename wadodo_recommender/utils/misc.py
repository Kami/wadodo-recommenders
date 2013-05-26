__all__ = [
    'ClassRepresentationMixin',
    'cls_to_str'
]


class ClassRepresentationMixin(object):

    def __unicode__(self):
        return cls_to_str(self)

    def __str__(self):
        value = self.__unicode__().encode('utf-8')
        return value


def cls_to_str(cls, attributes=None):
    """
    Return user friendly string representation for a class.
    """
    if attributes is None:
        attributes = [a for (a, _) in cls.__dict__.items()
                      if not a.startswith('_')]

    attributes_str = []

    for attribute in attributes:
        value = getattr(cls, attribute)
        attributes_str.append('%s=%s' % (attribute, value))

    attributes_str = ', '.join(attributes_str)
    result = '<%s %s>' % (cls.__class__.__name__, attributes_str)
    return result
