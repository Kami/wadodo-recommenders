#!/usr/bin/env python

from __future__ import absolute_import

import os
import json
from os.path import join as pjoin
from optparse import OptionParser

import facebook

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
BASE_FIXTURES_PATH = os.path.realpath(pjoin(CURRENT_PATH,
                                      '../tests/fixtures/providers/facebook/'))

REQUIRED_ARGUMENTS = ['token', 'directory']

OBJECTS = {
    'profile': {
        'name': 'me',
        'fields': []
    },
    'likes': {
        'name': 'me/likes',
        'fields': ['name', 'category', 'description']
    },
    'groups': {
        'name': 'me/groups',
        'fields': []
    },
    'interests': {
        'name': 'me/interests',
        'fields': []
    },
    'activities': {
        'name': 'me/activities',
        'fields': []
    }
}


def get_and_write_data(token, directory):
    graph = facebook.GraphAPI(token)

    for alias, value in OBJECTS.items():
        name = value['name']
        fields = value['fields']

        data = graph.get_object(name, fields=fields)
        file_name = '%s.json' % (alias)
        file_path = pjoin(BASE_FIXTURES_PATH, directory, file_name)
        write_fixture(data, file_path)


def write_fixture(data, file_path):
    print 'Writing fixture: %s ... ' % (file_path)
    data = json.dumps(data, sort_keys=True, indent=4)

    with open(file_path, 'w') as fp:
        fp.write(data)


def main():
    usage = 'usage: %prog --token=<oauth access token> --directory=<directory>'
    parser = OptionParser(usage=usage)
    parser.add_option('--token', dest='token',
                      help='OAuth access token')
    parser.add_option('--directory', dest='directory',
                      help='Directory where to store fixtures')

    (options, args) = parser.parse_args()

    for key in REQUIRED_ARGUMENTS:
        if not getattr(options, key, None):
            raise ValueError('Missing required argument: ' + key)

    fixtures_directory = pjoin(BASE_FIXTURES_PATH, options.directory)

    if not os.path.exists(fixtures_directory):
        os.makedirs(fixtures_directory)

    get_and_write_data(options.token, options.directory)

main()
