from graph_business_trip import __version__
from graph_business_trip.code import *


def test_version():
    assert __version__ == '0.1.0'


def test_1():
    g=Graphs()
    a=g.add_node('Pandora')
    b=g.add_node('Arendelle')
    c=g.add_node('Metroville')
    d=g.add_node('Monstropolis')
    e=g.add_node('Naboo')
    f=g.add_node('Narnia')

    g.add_edge(a,b,150)
    g.add_edge(b,a,150)
    g.add_edge(a,c,82)   
    g.add_edge(c,a,82)   
    g.add_edge(b,c,99)
    g.add_edge(c,b,99)
    g.add_edge(b,d,42)
    g.add_edge(d,b,42)
    g.add_edge(c,d,105)
    g.add_edge(d,c,105)
    g.add_edge(c,e,26)
    g.add_edge(e,c,26)
    g.add_edge(c,f,37)
    g.add_edge(f,c,37)
    g.add_edge(d,e,73)
    g.add_edge(e,d,73)
    g.add_edge(e,f,250)
    g.add_edge(f,e,250)
    
    g1 = ['Metroville', 'Pandora',]
    assert graph_business_trip(g,g1)=='True,$82'

    g2 = ['Arendelle', 'Monstropolis', 'Naboo']
    assert graph_business_trip(g,g2)=='True,$115'

    g3 = ['Naboo', 'Pandora']
    assert graph_business_trip(g,g3)=='False,$0'

    g4 = ['Narnia', 'Arendelle', 'Naboo']
    assert graph_business_trip(g,g4)=='False,$0'


def test_2():
    g=Graphs()
    a=g.add_node('a')
    b=g.add_node('b')
    c=g.add_node('c')

    g.add_edge(a,b,5)
    g.add_edge(b,c,4)  
    g.add_edge(c,a,3)
    g.add_edge(b,a,1)

    assert graph_business_trip(g,[a,b])=="True,$5"       