from confduino.boardinstall import install_board
from confduino.util import AutoBunch
from entrypoint2 import entrypoint

TEMPL = '{mcu}@{f_cpu} programmer:{upload}'


@entrypoint
def install(
    board_id='atmega88',
    mcu='atmega88',
    f_cpu=20000000,
    upload='usbasp',
    core='arduino',
    replace_existing=True,
):
    'install atmega88 board'

    board = AutoBunch()
    board.name = TEMPL.format(mcu=mcu, f_cpu=f_cpu, upload=upload)

    board.upload.using = upload
    board.upload.maximum_size = 8 * 1024

    board.build.mcu = mcu
    board.build.f_cpu = str(f_cpu) + 'L'
    board.build.core = core

    # for 1.0
    board.build.variant = 'standard'

    install_board(board_id, board, replace_existing=replace_existing)
