from bunch import unbunchify
from confduino import arduino_path
from confduino.util import read_properties
from entrypoint2 import entrypoint
from pprint import pprint
import logging

log = logging.getLogger(__name__)

def programmers_txt():
    'path of programmers.txt'
    x = arduino_path() / 'hardware' / 'arduino' / 'programmers.txt'
    assert x.exists()
    return x

def programmers():
    ''' read programmers from programmers.txt'''
    return read_properties(programmers_txt())

@entrypoint
def print_programmers():
    ''' print programmers from programmers.txt'''
    pprint( unbunchify(programmers()))
