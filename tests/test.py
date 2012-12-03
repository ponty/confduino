from confduino.boardinstall import install_board
from confduino.boardlist import print_boards, boards, board_names
from confduino.boardremove import remove_board
from confduino.hwpacklist import print_hwpacks, hwpacks, hwpack_names
from confduino.libinstall import install_lib
from confduino.liblist import print_libraries, libraries
from confduino.libremove import remove_lib
from confduino.mculist import print_mcus
from confduino.proginstall import install_programmer
from confduino.proglist import print_programmers, programmers
from confduino.progremove import remove_programmer
from confduino.util import tmpdir, ConfduinoError
from confduino.version import print_version, version
from nose.tools import eq_
from path import path
from unittest import TestCase
import os


class Test(TestCase):

    def test_lib(self):
        url = 'http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip'
        f = path(__file__).parent / 'data' / 'PS2Keyboard002.zip'
        d = tmpdir(suffix='_test')
        os.environ['ARDUINO_HOME'] = d

        (d / 'libraries').makedirs()
        eq_(libraries(), [])

        install_lib(url)
        eq_(libraries(), ['PS2Keyboard'])

        remove_lib('PS2Keyboard')
        eq_(libraries(), [])

        install_lib(f)
        eq_(libraries(), ['PS2Keyboard'])

        try:
            install_lib(f)
            assert 0
        except ConfduinoError:
            # OK
            eq_(libraries(), ['PS2Keyboard'])

    def test_prog(self):
        d = tmpdir(suffix='_test')
        os.environ['ARDUINO_HOME'] = d
        programmers_txt = d / 'hardware' / 'arduino' / 'programmers.txt'

        programmers_txt.parent.makedirs()

        programmers_txt.write_text('')
        eq_(programmers().keys(), [])

        programmers_txt.write_text('''
brd.x1.y1=foo
brd.x2=foo
brd.x3=foo
        ''')
        eq_(programmers().keys(), ['brd'])

        install_programmer('ardu', dict(x1='hi'))
        eq_(programmers().keys(), ['brd', 'ardu'])

        install_programmer('ardu', dict(x1='hi'))
        eq_(programmers().keys(), ['brd', 'ardu'])

        remove_programmer('brd')
        eq_(programmers().keys(), ['ardu'])

    def test_boards(self):
        d = tmpdir(suffix='_test')
        os.environ['ARDUINO_HOME'] = d
        boards_txt = d / 'hardware' / 'arduino' / 'boards.txt'

        boards_txt.parent.makedirs()

        boards_txt.write_text('')
        eq_(board_names(), [])
        eq_(boards().keys(), [])

        # invalid board
        boards_txt.write_text('''
brd.x3=foo
        ''')
        eq_(board_names(), [])

        boards_txt.write_text('''
brd.name=foo
brd.build=foo
brd.x3=foo
        ''')
        eq_(board_names(), ['brd'])
        eq_(boards().keys(), ['brd'])

        # invalid
        install_board('ardu', dict(x1='hi'))
        eq_(board_names(), ['brd'])

        install_board('ardu', dict(name='hi', build=1))
        eq_(set(board_names()), set(['brd', 'ardu']))

        install_board('ardu', dict(x1='hi'))
        eq_(set(board_names()), set(['brd', 'ardu']))

        remove_board('brd')
        eq_(board_names(), ['ardu'])

    def test_packs(self):
        d = tmpdir(suffix='_test')
        os.environ['ARDUINO_HOME'] = d
        (d / 'hardware').makedirs()
        eq_(hwpack_names(), [])
        boards_txt = d / 'hardware' / 'p1' / 'boards.txt'
        boards_txt.parent.makedirs()
        boards_txt.write_text('')
        eq_(hwpack_names(), ['p1'])
        boards_txt = d / 'hardware' / 'p2' / 'boards.txt'
        boards_txt.parent.makedirs()
        boards_txt.write_text('')
        eq_(hwpack_names(), ['p1', 'p2'])

    def test_version(self):
        d = tmpdir(suffix='_test')
        os.environ['ARDUINO_HOME'] = d
        (d / 'lib').makedirs()
        v = d / 'lib' / 'version.txt'
        v.write_text('0017')
        eq_(int(version()), 17)
        v.write_text('\n0018\n')
        eq_(int(version()), 18)
