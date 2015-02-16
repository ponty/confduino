from confduino import arduino_path
from confduino.util import read_properties
from entrypoint2 import entrypoint
from confduino.prettyprint import pp
import logging

log = logging.getLogger(__name__)


def boards_txt(hwpack='arduino'):
    """path of boards.txt."""
    x = arduino_path() / 'hardware' / hwpack / 'boards.txt'
    assert x.exists(), x
    return x


def boards(hwpack='arduino'):
    """read boards from boards.txt.

    :param core_package: 'all,'arduino',..

    """
    bunch = read_properties(boards_txt(hwpack))

    bunch_items = list(bunch.items())

    # remove invalid boards
    for bid, board in bunch_items:
        if 'build' not in board.keys() or 'name' not in board.keys():
            log.debug('invalid board found: %s', bid)
            del bunch[bid]

    return bunch


def board_names(hwpack='arduino'):
    """return installed board names."""
    ls = list(boards(hwpack).keys())
    ls.sort()
    return ls


@entrypoint
def print_boards(hwpack='arduino', verbose=False):
    """print boards from boards.txt."""
    if verbose:
        pp(boards(hwpack))
    else:
        print('\n'.join(board_names(hwpack)))
