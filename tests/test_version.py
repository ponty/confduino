from confduino import set_arduino_path
from confduino.version import version, intversion
from nose.tools import eq_
from data import TEST_ARDUINO_INSTALLATIONS


def test_ver2():
    for x in TEST_ARDUINO_INSTALLATIONS:
        print (x)
        set_arduino_path(x.path)
        eq_(version(), x.ver)


def test_iver():
    eq_(intversion('0022'), 22)
    eq_(intversion('0023'), 23)
    eq_(intversion('0001'), 1)
    eq_(intversion('0022ubuntu0.1'), 22)
    eq_(intversion('1.0'), 100)
    eq_(intversion('1.0.3'), 103)
    eq_(intversion('3.2.1'), 321)


def test_iver2():
    for x in TEST_ARDUINO_INSTALLATIONS:
        print (x)
        set_arduino_path(x.path)
        eq_(intversion(), x.iver)
