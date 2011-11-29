from confduino import arduino_path
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)

def examples_dir():
    '''return arduino/examples directory 

    :rtype: string
    '''
    x = arduino_path() / 'examples'
    return x

def examples_all_dir():
    '''return arduino/examples/all directory 

    :rtype: string
    '''
    x = examples_dir() / 'all'
    return x

