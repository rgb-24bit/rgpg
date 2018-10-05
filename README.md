# rgpg

> Generate the password with the necessary information and the specified input.

# Install

First clone this repository:
```
$ git clone https://github.com/rgb-24bit/rgpg.git
```

Then edit the file [Essential.java](rgpg/src/main/java/org/rgbit/rgpg/Essential.java), this is your configuration file.

I don't want to introduce more cost of parsing the configuration file, so I use this Java class directly as the necessary configuration file.

Finally, execute the following command:
```
$ ./gradlew installDist
```

The generated file will be located `build/install`.

# Usage

```
Usage: rgpg [OPTIONS]... STRING

Generate a password based on the specified character

Options:
  -l, --length  specify the length of the password.
                Valid values range from 1-32.
  -h, --help    display this help and exit.
```

