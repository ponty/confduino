from bunch import unbunchify
from confduino.boardlist import boards, board_names
from confduino.hwpacklist import hwpack_names
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)

           
def mcus():
    '''MCU list
    '''
    ls = []
    for h in hwpack_names():
        for b in board_names(h):
            ls += [mcu(b, h)]
    ls = sorted(list(set(ls)))
    return ls
  
def mcu(board_id, hwpack_id):
    '''
    '''
    board = boards(hwpack=hwpack_id)[board_id]
    return board.build.mcu

@entrypoint
def print_mcus():
    ''' print boards from boards.txt'''
    ls = unbunchify(mcus())
    print '\n'.join(ls)
