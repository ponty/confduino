from confduino.boardlist import board_names
from confduino.boardlist import boards_txt
from confduino.boardremove import remove_board
from confduino.hwpacklist import hwpack_names
from entrypoint2 import entrypoint
import psidialogs


@entrypoint
def remove_boards_gui(hwpack=''):
    """remove boards by GUI."""
    if not hwpack:
        if len(hwpack_names()) > 1:
            hwpack = psidialogs.choice(hwpack_names(),
                                       'select hardware package to select board from!',
                                       title='select')
        else:
            hwpack = hwpack_names()[0]
    print('%s selected' % hwpack)

    if hwpack:
        sel = psidialogs.multi_choice(board_names(hwpack),
                                      'select boards to remove from %s!' % boards_txt(
                                          hwpack),
                                      title='remove boards')
        print('%s selected' % sel)

        if sel:
            for x in sel:
                remove_board(x)
                print('%s was removed' % x)
