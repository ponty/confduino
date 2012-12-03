from confduino import set_arduino_path
from confduino.version import version, intversion
from easyprocess import Proc
from nose.tools import eq_

# def test_ver():
#    eq_(Proc('python -m confduino.version').call().stdout,'0022')


def test_ver2():
    set_arduino_path('~/opt/arduino-0022')
    eq_(version(), '0022')
    set_arduino_path('~/opt/arduino-0023')
    eq_(version(), '0023')
    set_arduino_path('~/opt/arduino-1.0')
    eq_(version(), '1.0')
    set_arduino_path('/usr/share/arduino/')
    eq_(version(), '0022ubuntu0.1')


def test_iver():
    eq_(intversion('0022'), 22)
    eq_(intversion('0023'), 23)
    eq_(intversion('0001'), 1)
    eq_(intversion('0022ubuntu0.1'), 22)
    eq_(intversion('1.0'), 100)
    eq_(intversion('12.51'), 1251)
