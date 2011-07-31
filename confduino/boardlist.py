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
    assert x.exists(), x
    return x
            
def boards():
    ''' read boards from boards.txt
    
    example::
    
        {
        'atmega328': {'bootloader': {'extended_fuses': '0x05',
                                     'file': 'ATmegaBOOT_168_atmega328.hex',
                                     'high_fuses': '0xDA',
                                     'lock_bits': '0x0F',
                                     'low_fuses': '0xFF',
                                     'path': 'atmega',
                                     'unlock_bits': '0x3F'},
                      'build': {'core': 'arduino',
                                'f_cpu': '16000000L',
                                'mcu': 'atmega328p'},
                      'name': 'Arduino Duemilanove or Nano w/ ATmega328',
                      'upload': {'maximum_size': '30720',
                                 'protocol': 'stk500',
                                 'speed': '57600'}},
     
        'mini': {'bootloader': {'extended_fuses': '0x00',
                                'file': 'ATmegaBOOT_168_ng.hex',
                                'high_fuses': '0xdd',
                                'lock_bits': '0x0F',
                                'low_fuses': '0xff',
                                'path': 'atmega',
                                'unlock_bits': '0x3F'},
                 'build': {'core': 'arduino',
                           'f_cpu': '16000000L',
                           'mcu': 'atmega168'},
                 'name': 'Arduino Mini',
                 'upload': {'maximum_size': '14336',
                            'protocol': 'stk500',
                            'speed': '19200'}},
        }
    
    '''
    return read_properties(boards_txt())

@entrypoint
def print_boards():
    ''' print boards from boards.txt'''
    pprint(unbunchify(boards()))

def mcu(board_name):
    return  boards()[board_name].build.mcu

def f_cpu(board_name):
    return  boards()[board_name].build.f_cpu

def targets():
    ls = [mcu(x) for x in boards().keys()]
    ls = sorted(list(set(ls)))
    return ls
    
