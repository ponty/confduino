from bunch import unbunchify
from confduino.boardlist import boards, board_names
from confduino.hwpacklist import hwpacks, hwpack_names
from entrypoint2 import entrypoint
from pprint import pprint
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

@entrypoint
def print_mcus():
    ''' print boards from boards.txt'''
    pprint(unbunchify(mcus()))

   
def mcu(board_id, hwpack_id):
    '''
    '''
    board = boards(hwpack=hwpack_id)[board_id]
    return board.build.mcu
