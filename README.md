# rgpg

> Password generator to generate a password based on the specified pattern.

## Usage

```
usage: rgpg [-h] [-v] -p PATTERN -k KEY

Password generator to generate a password basedon the specified pattern.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -p PATTERN, --pattern PATTERN
                        The mode used to generate the password.
  -k KEY, --key KEY     The base key used to generate the password.
```

The syntax of the pattern is:
1. Specify the number of special, uppercase, lowercase, and numeric characters by S, U, L, D and integers.
2. Characters are not case sensitive.
3. Characters can be repeated.

Example:
```
$ rgpg -k key -p s1u2l3d4l3u2s1
4V_4en@SGnv3Yff9
```

## Install

Install by downloading the source code.

```
$ git clone https://github.com/rgb-24bit/rgpg.git
$ cd rgpg
$ python setup.py install
```

## History

See [releases](https://github.com/rgb-24bit/rgpg/releases) page.

## LICENSE

MIT License.
