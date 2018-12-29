# -*- coding: utf-8 -*-

"""
Implement password generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2018 by rgb-24bit.
:license: MIT, see LICENSE for more details.
"""

from hashlib import md5


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
