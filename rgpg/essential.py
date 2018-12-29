# -*- coding: utf-8 -*-

"""
Provide the necessary information for the password generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2018 by rgb-24bit.
:license: GPL 3.0, see LICENSE for more details.
"""

import json


class Essential(object):
    def __init__(self):
        self.__dict__ = {
            # The base string used to generate the MD5 digest
            'K1': '123456',
            'K2': '',
            'K3': '',

            # Specify the first character of the generated password
            'FIRST': 'K',

            # The character to be replaced by the `str.translate` method and its target
            'TRANS_SRC': '1234567890abcdef',
            'TRANS_DST': 'abcdef1234567890'
        }

    def makefile(self, path):
        """Create a profile based on an existing configuration."""
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, indent=4)

    def loadfile(self, path):
        """Load the configuration in the specified configuration file.

        Return:
            The update succeeds and returns True. The file format error returns False.
        """
        try:
            with open(path, encoding='utf-8') as f:
                self.__dict__.update(json.load(f))
        except Exception as e:
            return False
        return True

    def __repr__(self):
        return 'Essential: %r' % self.__dict__
