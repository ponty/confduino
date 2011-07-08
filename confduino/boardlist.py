from bunch import unbunchify
from confduino import arduino_path
from confduino.util import read_properties
from entrypoint2 import entrypoint
from pprint import pprint
import logging

log = logging.getLogger(__name__)

def boards_txt():
    'path of boards.txt'
    x = arduino_path() / 'hardware' / 'arduino' / 'boards.txt'
    assert x.exists(),x
    return x
            
def boards():
    ''' read boards from boards.txt'''
    return read_properties(boards_txt())

@entrypoint
def print_boards():
    ''' print boards from boards.txt'''
    pprint( unbunchify(boards()))
