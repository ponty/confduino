from confduino import arduino_path
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)

def libraries_dir():
    'return library root path'
    x = arduino_path() / 'libraries'
    assert x.exists(), x
    return x

def libraries():
    'return installed library names'
    ls = libraries_dir().listdir()
    ls = [x.name for x in ls]
    ls.sort()
    return ls

@entrypoint
def print_libraries():
    'print installed arduino libraries'
    print '\n'.join(libraries())
