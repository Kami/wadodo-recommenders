__all__ = [
    'born_str_to_age'
]

import datetime


def date_str_to_date(date_str):
    """
    Return date object for the date in the following format - mm/dd/yyyy.
    """
    split = date_str.split('/')
    date = datetime.date(month=int(split[0]), day=int(split[1]),
                         year=int(split[2]))
    return date


def born_str_to_age(born_str):
    """
    Return age in years for the born string in format mm/dd/yyyy.
    """
    born = date_str_to_date(born_str)
    today = datetime.date.today()

    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        # raised when birth date is February 29 and the current year is not a
        # leap year
        birthday = born.replace(year=today.year, day=(born.day - 1))

    if birthday > today:
        return ((today.year - born.year) - 1)
    else:
        return (today.year - born.year)
