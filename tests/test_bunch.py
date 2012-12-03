from confduino.util import AutoBunch, bunch2properties
from nose.tools import eq_


def test_1():
    x = AutoBunch()
    eq_(x.keys(), [])

    x.a = 3
    eq_(x.keys(), ['a'])
    eq_(x['a'], 3)
    eq_(x.a, 3)


def test_2():
    x = AutoBunch()
    x.a.b = 3
    eq_(x.keys(), ['a'])
    eq_(x['a']['b'], 3)
    eq_(x.a.b, 3)
    eq_(x['a'].b, 3)
    eq_(x.a['b'], 3)

    lines = bunch2properties('x', x)
