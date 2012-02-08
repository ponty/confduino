from confduino.boardlist import print_boards
from confduino.hwpacklist import print_hwpacks
from confduino.liblist import print_libraries
from confduino.mculist import print_mcus
from confduino.proglist import print_programmers
from confduino.version import print_version
from nose.tools import eq_
from unittest import TestCase
import os

class Test(TestCase):
    def test_print(self):
        if 'ARDUINO_HOME' in os.environ:
            del os.environ['ARDUINO_HOME']
        print_libraries()        
        print_boards()        
        print_programmers()        
        print_hwpacks()        
        print_mcus()
#        print_version()

def test_cli():
    if 'ARDUINO_HOME' in os.environ:
        del os.environ['ARDUINO_HOME']
    eq_(os.system('python -m confduino.boardlist'), 0)
    eq_(os.system('python -m confduino.boardlist --verbose'), 0)
    eq_(os.system('python -m confduino.hwpacklist'), 0)
    eq_(os.system('python -m confduino.proglist'), 0)
    eq_(os.system('python -m confduino.proglist --verbose'), 0)
    eq_(os.system('python -m confduino.boardlist'), 0)
    eq_(os.system('python -m confduino.liblist'), 0)
    eq_(os.system('python -m confduino.mculist'), 0)
