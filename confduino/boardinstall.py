from confduino.boardlist import boards_txt, boards
from confduino.boardremove import remove_board
from confduino.util import bunch2properties
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)

# TODO: how to pass options as cli argument?
       
def install_board(board_id, board_options, hwpack='arduino', replace_existing=False):
    '''install board in boards.txt
    
    :param board_id: string identifier
    :param board_options: dict like
    :param replace_existing: bool
    :rtype: None
    '''       
    doaction = 0
    if board_id in boards(hwpack).keys():
        log.debug('board already exists:' + board_id)
        if replace_existing:
            log.debug('remove board: %s' % (board_id))
            remove_board(board_id)
            doaction = 1
    else:
        doaction = 1
        
    if doaction:
        lines = bunch2properties(board_id, board_options)
        boards_txt().write_lines([''] + lines, append=1)
    
    
    
    
