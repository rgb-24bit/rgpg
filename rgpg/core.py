# -*- coding: utf-8 -*-

import json

from hashlib import md5


class Essential(object):
    "Provide the necessary information for the password generator."
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


def md5_hexdigest(a, b):
    """MD5 `a + b` and return hexdigest str."""
    return md5((a + b).encode('utf-8')).hexdigest()


def generate(key, essential, length=16):
    """Password generator."""
    md5k1 = md5_hexdigest(essential.K1, key)
    md5k2 = md5_hexdigest(essential.K2, md5k1)
    md5k3 = md5_hexdigest(essential.K3, md5k1)

    password = ''.join(map(max, zip(md5k2, md5k3)))

    table = str.maketrans(essential.TRANS_SRC, essential.TRANS_DST)
    return essential.FIRST + password[1: min(length, 32)].translate(table)
