from confduino import arduino_path
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)

def nocase_subitem(dir, name):
    for x in dir.listdir():
        if x.name.lower() == name.lower():
            return x
    return dir / name

def libraries_dir():
    '''return library root path
    
    $ARDUINO/libraries
    '''
    x = arduino_path() / 'libraries'
    assert x.exists(), x
    return x

def libraries():
    'return installed library names'
    ls = libraries_dir().dirs()
    ls = [x.name for x in ls]
    ls.sort()
    return ls

def lib_dir(lib):
    '''return library directory
    
    $ARDUINO/libraries/$LIB
    '''
    return libraries_dir() / lib

def lib_examples_dir(lib):
    '''return library examples directory
    
    $ARDUINO/libraries/$LIB/examples
    '''
    return nocase_subitem(lib_dir(lib) , 'examples')

def lib_example_dir(lib, example):
    '''return library example directory
    
    $ARDUINO/libraries/$LIB/examples/$EXAMPLE
    '''
    return lib_examples_dir(lib) / example
    
def lib_examples(lib):
    '''return library examples 
    
    EXAMPLE1,EXAMPLE2,..
    '''
    d = lib_examples_dir(lib)
    if not d.exists():
        return []
    ls = d.dirs()
    ls = [x.name for x in ls]
    ls.sort()
    return ls

@entrypoint
def print_libraries():
    'print installed arduino libraries'
    print '\n'.join(libraries())
