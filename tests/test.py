from confduino.boardinstall import install_board
from confduino.boardlist import print_boards, boards
from confduino.boardremove import remove_board
from confduino.libinstall import install_lib
from confduino.liblist import print_libraries, libraries
from confduino.libremove import remove_lib
from confduino.proginstall import install_programmer
from confduino.proglist import print_programmers, programmers
from confduino.progremove import remove_programmer
from confduino.util import tmpdir
from nose.tools import eq_
from path import path
from unittest import TestCase
import os


class Test(TestCase):
    def test_print(self):
        if 'ARDUINO_HOME' in os.environ:
            del os.environ['ARDUINO_HOME']
        print_libraries()        
        print_boards()        
        print_programmers()        
        
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

        install_lib(f)
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

        install_programmer('ardu',dict(x1='hi'))
        eq_(programmers().keys(), ['brd','ardu'])

        install_programmer('ardu',dict(x1='hi'))
        eq_(programmers().keys(), ['brd','ardu'])

        remove_programmer('brd')
        eq_(programmers().keys(), ['ardu'])

    
    def test_boards(self):
        d = tmpdir(suffix='_test')
        os.environ['ARDUINO_HOME'] = d
        boards_txt = d / 'hardware' / 'arduino' / 'boards.txt'        
        
        boards_txt.parent.makedirs()        

        boards_txt.write_text('')
        eq_(boards().keys(), [])
        
        boards_txt.write_text('''
brd.x1=foo
brd.x2=foo
brd.x3=foo
        ''')
        eq_(boards().keys(), ['brd'])

        install_board('ardu',dict(x1='hi'))
        eq_(boards().keys(), ['brd','ardu'])

        install_board('ardu',dict(x1='hi'))
        eq_(boards().keys(), ['brd','ardu'])

        remove_board('brd')
        eq_(boards().keys(), ['ardu'])










        
