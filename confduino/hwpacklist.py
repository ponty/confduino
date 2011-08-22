from confduino import arduino_path
from confduino.boardlist import boards
from confduino.util import AutoBunch
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)

def hwpack_dir():
    'return hardware packages root path'
    x = arduino_path() / 'hardware'
    assert x.exists(), x
    return x

def hwpacks():
    '''
        example::
    
{'Sanguino': {'sanguino': {'bootloader': {'extended_fuses': '0xFD',
                                          'file': 'ATmegaBOOT_644P.hex',
                                          'high_fuses': '0xDC',
                                          'lock_bits': '0x0F',
                                          'low_fuses': '0xFF',
                                          'path': 'atmega644p',
                                          'unlock_bits': '0x3F'},
                           'build': {'core': 'arduino',
                                     'f_cpu': '16000000L',
                                     'mcu': 'atmega644p'},
                           'name': 'Sanguino',
                           'upload': {'maximum_size': '63488',
                                      'protocol': 'stk500',
                                      'speed': '38400'}}},
 'arduino': {'atmega8': {'bootloader': {'file': 'ATmegaBOOT.hex',
                                        'high_fuses': '0xca',
                                        'lock_bits': '0x0F',
                                        'low_fuses': '0xdf',
                                        'path': 'atmega8',
                                        'unlock_bits': '0x3F'},
                         'build': {'core': 'arduino',
                                   'f_cpu': '16000000L',
                                   'mcu': 'atmega8'},
                         'name': 'Arduino NG or older w/ ATmega8',
                         'upload': {'maximum_size': '7168',
                                    'protocol': 'stk500',
                                    'speed': '19200'}},
             'uno': {'bootloader': {'extended_fuses': '0x05',
                                    'file': 'optiboot_atmega328.hex',
                                    'high_fuses': '0xde',
                                    'lock_bits': '0x0F',
                                    'low_fuses': '0xff',
                                    'path': 'optiboot',
                                    'unlock_bits': '0x3F'},
                     'build': {'core': 'arduino',
                               'f_cpu': '16000000L',
                               'mcu': 'atmega328p'},
                     'name': 'Arduino Uno',
                     'upload': {'maximum_size': '32256',
                                'protocol': 'stk500',
                                'speed': '115200'}}},
 'arduino-extras': {'arduino_amber128': {'bootloader': {'extended_fuses': '0xFF',
                                                        'file': 'stk500boot_v2_amber128.hex',
                                                        'high_fuses': '0xC8',
                                                        'lock_bits': '0x0F',
                                                        'low_fuses': '0x8F',
                                                        'path': 'atmega',
                                                        'unlock_bits': '0x3F'},
                                         'build': {'core': 'arduino',
                                                   'f_cpu': '14745600L',
                                                   'mcu': 'atmega128'},
                                         'name': 'Arduino-Amber 128 14.7456 Mhz',
                                         'upload': {'maximum_size': '122880',
                                                    'protocol': 'stk500v2',
                                                    'speed': '115200'}},
                       'stk525_647': {'build': {'core': 'arduino',
                                             'f_cpu': '8000000L',
                                             'mcu': 'at90usb647',
                                             'post_compile_script': 'teensy_post_compile'},
                                   'name': 'STK500 w/STK525 - at90usb647 (Arduino Core)',
                                   'upload': {'avrdude_wrapper': 'teensy_reboot',
                                              'disable_flushing': 'true',
                                              'maximum_size': '56000',
                                              'protocol': 'halfkay',
                                              'speed': '38400'}}}}
    '''
    bunch = AutoBunch()
    for x in hwpack_names():
        bunch[x] = boards(x)
    return bunch

def hwpack_names():
    'return installed hardware package names'
    ls = hwpack_dir().listdir()
    ls = [x.name for x in ls]
    ls = [x for x in ls if x != 'tools']
    arduino_included='arduino' in ls
    ls = [x for x in ls if x != 'arduino']
    ls.sort()
    if arduino_included:
        ls = ['arduino'] + ls # move to 1st pos
    return ls

@entrypoint
def print_hwpacks():
    'print installed arduino hardware packages'
    print '\n'.join(hwpack_names())
