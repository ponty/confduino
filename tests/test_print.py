from confduino.boardlist import print_boards
from confduino.hwpacklist import print_hwpacks
from confduino.liblist import print_libraries
from confduino.mculist import print_mcus
from confduino.proglist import print_programmers
from confduino.version import print_version
from nose.tools import eq_
from data import TEST_ARDUINO_PATHS
import os


def test_print():
    for x in TEST_ARDUINO_PATHS:
        os.environ['ARDUINO_HOME'] = x
        print 'ARDUINO_HOME=', x

        print_boards()
        print_hwpacks()
        print_libraries()
        print_mcus()
        print_programmers()
        print_version()


def test_cli():
    for x in TEST_ARDUINO_PATHS:
        os.environ['ARDUINO_HOME'] = x
        print 'ARDUINO_HOME=', x

        eq_(os.system('python -m confduino.boardlist'), 0)
        eq_(os.system('python -m confduino.boardlist --verbose'), 0)
        eq_(os.system('python -m confduino.hwpacklist'), 0)
        eq_(os.system('python -m confduino.proglist'), 0)
        eq_(os.system('python -m confduino.proglist --verbose'), 0)
        eq_(os.system('python -m confduino.boardlist'), 0)
        eq_(os.system('python -m confduino.liblist'), 0)
        eq_(os.system('python -m confduino.mculist'), 0)
