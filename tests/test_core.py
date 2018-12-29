# -*- coding: utf-8 -*-

import os

from rgpg.core import Essential, md5_hexdigest, generate


def test_essential():
    essential = Essential()

    essential.makefile('temp.json')
    assert os.path.isfile('temp.json')

    assert essential.loadfile('temp.json')

    assert essential.FIRST == 'K'

    os.remove('temp.json')


def test_md5_hexdigest():
    assert len(md5_hexdigest('abc', 'cbd')) == 32
    assert isinstance(md5_hexdigest('', ''), str)


def test_generate():
    essential = Essential()

    passwd = generate('key', essential)
    assert passwd[0] == essential.FIRST
    assert len(passwd) == 16

    passwd = generate('key', essential, 33)
    assert len(passwd) == 32
