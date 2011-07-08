from confduino.boardlist import boards_txt
from entrypoint2 import entrypoint
from path import path
import logging

log = logging.getLogger(__name__)

@entrypoint
def remove_board(board_id):
    '''remove board
    
    :param board_id: board id (e.g. 'diecimila')
    :rtype: None
    '''

    log.debug('remove %s' % (board_id))
    lines = boards_txt().lines()
    lines = filter(lambda x: not x.strip().startswith(board_id + '.'), lines)
    boards_txt().write_lines(lines)