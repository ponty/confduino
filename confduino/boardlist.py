from bunch import unbunchify
from confduino import arduino_path
from confduino.util import read_properties
from entrypoint2 import entrypoint
from pprint import pprint
import logging

log = logging.getLogger(__name__)

def boards_txt(hwpack='arduino'):
    'path of boards.txt'
    x = arduino_path() / 'hardware' / hwpack / 'boards.txt'
    assert x.exists(), x
    return x
            
def boards(hwpack='arduino'):
    ''' read boards from boards.txt
    
    
    :param core_package: 'all,'arduino',..
    '''
    bunch = read_properties(boards_txt(hwpack))
        
    # remove invalid boards
    for bid, board in bunch.items():
        log.debug('    board found:' + bid)
        if not 'build' in board.keys() or  not 'name' in board.keys():
            log.debug('invalid board found:' + bid)
            del bunch[bid]
        
    return bunch

def board_names(hwpack='arduino'):
    'return installed board names'
    ls = boards(hwpack).keys()
    ls.sort()
    return ls

@entrypoint
def print_boards(hwpack='arduino', verbose=False):
    ''' print boards from boards.txt'''
    if verbose:
        pprint(unbunchify(boards(hwpack)),width=1)
    else:
        print('\n'.join(board_names(hwpack)))
    
