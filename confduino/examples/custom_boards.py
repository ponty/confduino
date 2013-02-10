from __future__ import division
from confduino.boardinstall import install_board
from confduino.util import AutoBunch
from entrypoint2 import entrypoint

TEMPL_NAME = '{mcu}@{f_cpu}'
TEMPL_ID = '{mcu}_{f_cpu}'


def format_freq(f):
    if f >= 1000000:
        f = f / 1000000.0
        suffix = 'MHz'
    elif f >= 1000:
        f = f / 1000.0
        suffix = 'kHz'
    else:
        suffix = 'Hz'
    f = ('%f' % f).rstrip('0').rstrip('.')
    return f + '' + suffix


@entrypoint
def main(
    upload='usbasp',
    core='arduino',
    replace_existing=True,
):
    'install custom boards'

    def install(mcu, f_cpu, kbyte):
        board = AutoBunch()
        board.name = TEMPL_NAME.format(mcu=mcu,
                                       f_cpu=format_freq(f_cpu),
                                       upload=upload)
        board_id = TEMPL_ID.format(mcu=mcu,
                                   f_cpu=(f_cpu),
                                   upload=upload)

        board.upload.using = upload
        board.upload.maximum_size = kbyte * 1024

        board.build.mcu = mcu
        board.build.f_cpu = str(f_cpu) + 'L'
        board.build.core = core

        # for 1.0
        board.build.variant = 'standard'

        install_board(board_id, board, replace_existing=replace_existing)

    install('atmega8', 1000000, 8)
    install('atmega8', 12000000, 8)
    install('atmega88', 1000000, 8)
    install('atmega88', 8000000, 8)
    install('atmega88', 12000000, 8)
    install('atmega88', 20000000, 8)
    install('atmega328p', 20000000, 32)
    install('atmega328p', 8000000, 32)
    install('atmega328p', 1000000, 32)
