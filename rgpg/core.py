# -*- coding: utf-8 -*-

import argparse
import hashlib
import string
import re

from rgpg.__version__ import __version__, __description__


def random_generator(str_seed: str):
    """Simple pseudo-random number generator."""
    seed = int(hashlib.md5(str_seed.encode(encoding='utf-8')).hexdigest()[:8], 16)
    multiplier, addend, mask = 0x5DEECE66D, 0xB, (1 << 48) - 1
    while True:
        seed = (seed * multiplier + addend) & mask
        yield seed >> 16


def generate_password(key: str, pattern: str):
    """Password generator to generate a password based on the specified pattern.

    The syntax of the pattern is:
    1. Specify the number of special, uppercase, lowercase, and numeric characters
       by S, U, L, D and integers.
    2. Characters are not case sensitive.
    3. Characters can be repeated.

    Example:
    >>> generate_password('key', 'S1U2L3D10')
    4v5463@SG313y5f9
    >>> generate_password('key', 'S1U2L3D4L3U2S1')
    4V_4en@SGnv3Yff9

    Args:
        key: The base key used to generate the password.
        pattern: The mode used to generate the password.

    Return:
        Returns the password generated according to the pattern.
    """
    _ascii_upper = string.ascii_uppercase
    _ascii_lower = string.ascii_lowercase
    _ascii_digit = string.digits
    _ascii_specl = "~!@#$%^&*_+"

    upper_count = 0
    lower_count = 0
    digit_count = 0
    specl_count = 0

    for match in re.findall(r'([SULD]\d+)', pattern.upper()):
        if match[0] == 'S':
            specl_count += int(match[1:])

        if match[0] == 'U':
            upper_count += int(match[1:])

        if match[0] == 'L':
            lower_count += int(match[1:])

        if match[0] == 'D':
            digit_count += int(match[1:])

    charset, random = [], random_generator(key)
    def fill_charset(count: int, chars: str):
        while count > 0:
            charset.append(chars[next(random) % len(chars)])
            count -= 1
    fill_charset(upper_count, _ascii_upper)
    fill_charset(lower_count, _ascii_lower)
    fill_charset(digit_count, _ascii_digit)
    fill_charset(specl_count, _ascii_specl)

    # Apply Knuth-Shuffle shuffling algorithm
    for i in range(len(charset) - 1, -1, -1):
        rand_i = next(random) % (i + 1)
        charset[i], charset[rand_i] = charset[rand_i], charset[i]

    return ''.join(charset)


def argparser():
    """Command line arguments parsing."""
    parser = argparse.ArgumentParser(prog='rgpg', description=__description__)

    parser.add_argument('-v', '--version',
                        action='version', version='%(prog)s ' + __version__)

    parser.add_argument('-p', '--pattern',
                        action='store', dest='pattern', type=str, required=True,
                        help='The mode used to generate the password.')

    parser.add_argument('-k', '--key',
                        action='store', dest='key', type=str, required=True,
                        help='The base key used to generate the password.')

    args = parser.parse_args()

    print(generate_password(args.key, args.pattern))


def cli():
    argparser()


if __name__ == '__main__':
    cli()
