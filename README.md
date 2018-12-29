# rgpg

> Generate the password with the necessary information and the specified input.

## Usage

```
usage: rgpg [-h] [-v] [-l LENGTH] [-f FILE] [-k KEY | -u URL | -c CREATE]

Generate the password with the necessary informationand the specified input.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -l LENGTH, --length LENGTH
                        Specify the length of the password
  -f FILE, --file FILE  Specify configuration file
  -k KEY, --key KEY     Generate a password based on the specified key
  -u URL, --url URL     Generate a password based on the specified url
  -c CREATE, --create CREATE
                        Create a default configuration profile
```

You can generate a default configuration file with the `-c` option and specify the configuration file that the password generator needs to use with the option `-f`.

If you do not specify a profile, the password generator will generate your password using the `default` configuration.

The option `-u` will intercept the host part of the specified url for password generation.

The option `-k` can be used to specify any string.

## Install

Install by downloading the source code.

```
$ git clone https://github.com/rgb-24bit/rgpg.git
$ cd rgpg
$ python setup.py install
```

## History

See [releases](https://github.com/rgb-24bit/rgpg/releases) page.

## TODO

- [ ] Specify individual configuration items through command line options
- [ ] Read file batch generation password

## LICENSE

MIT License.
