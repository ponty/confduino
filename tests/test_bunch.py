from confduino.boardlist import boards
from confduino.util import AutoBunch
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


#def test_boards2():
#    print boards().diecimila.build.f_cpu    
#    assert 0
#
#def test_boards3():
#    print boards().keys()    
#    print boards()   
#    assert 0





        
