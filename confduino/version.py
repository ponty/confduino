from confduino import arduino_path
from entrypoint2 import entrypoint


def version_txt():
    """return version.txt path.

    $ARDUINO/lib/version.txt

    """
    x = arduino_path() / 'lib' / 'version.txt'
    return x


def version():
    """return version as string.

    example: 0022

    """
    return version_txt().text().strip()


def intversion(text=None):
    """return version as int.

    0022 ->  22
    0022ubuntu0.1 ->  22
    0023 ->  23
    1.0  -> 100
    1.0.3  -> 103
    1:1.0.5+dfsg2-2 -> 105

    """
    try:
        s = text

        if not s:
            s = version()

        s = s.split('ubuntu')[0]
        s = s.split(':')[-1]
        s = s.split('+')[0]

        # <100
        if s.startswith('00'):
            i = int(s[0:4])
        # >=100
        elif '.' in s:
            ls = s.split('.')
            ls += [0, 0, 0]
            i = int(ls[0]) * 100 + int(ls[1]) * 10 + int(ls[2])
    except ValueError:
        print ('Can not parse version: %s' % text)
        raise
    return i


def sketch_extension():
    """.pde or .ino."""
    return '.ino' if intversion() >= 100 else '.pde'


def all_sketch_extensions():
    """['.pde','.ino']"""
    return ['.pde', '.ino']


@entrypoint
def print_version(integer=False):
    """print arduino version.

    example: 0022

    """
    if integer:
        print(intversion())
    else:
        print(version())
