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
    def check_print(cmd):
        cmd = 'python -m confduino.%s > /dev/null' % cmd
        print cmd
        eq_(os.system(cmd), 0)

    for x in TEST_ARDUINO_PATHS:
        os.environ['ARDUINO_HOME'] = x
        print 'ARDUINO_HOME=', x

        check_print('boardlist')
        check_print('boardlist --verbose')
        check_print('hwpacklist')
        check_print('proglist')
        check_print('proglist --verbose')
        check_print('boardlist')
        check_print('liblist')
        check_print('mculist')
