from confduino.util import AutoBunch, bunch2properties
from nose.tools import eq_


def check_keys(ls1, ls2):
    eq_(sorted(list(ls1)), ls2)


def test_1():
    x = AutoBunch()
    check_keys(x.keys(), [])

    x.a = 3
    check_keys(x.keys(), ['a'])
    eq_(x['a'], 3)
    eq_(x.a, 3)


def test_2():
    x = AutoBunch()
    x.a.b = 3
    check_keys(x.keys(), ['a'])
    eq_(x['a']['b'], 3)
    eq_(x.a.b, 3)
    eq_(x['a'].b, 3)
    eq_(x.a['b'], 3)

    lines = bunch2properties('x', x)


def test_setattr():
    x = AutoBunch()
    setattr(x, 'a.b', 3)
    check_keys(x.keys(), ['a'])
    eq_(x['a']['b'], 3)
    eq_(x.a.b, 3)
    eq_(x['a'].b, 3)
    eq_(x.a['b'], 3)

    lines = bunch2properties('x', x)
