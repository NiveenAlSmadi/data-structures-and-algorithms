from graph import __version__
from graph.graph import *
from graph.queue_and_stack import *

def test_version():
    assert __version__ == '0.1.0'

'''
Node can be successfully added to the graph
An edge can be successfully added to the graph
A collection of all nodes can be properly retrieved from the graph
All appropriate neighbors can be retrieved from the graph
Neighbors are returned with the weight between nodes included
The proper size is returned, representing the number of nodes in the graph
A graph with only one node and edge can be properly returned
An empty graph properly returns null

'''

def test_add_node():
    g = Graphs()
    assert 'niveen'== g.add_node('niveen').value

def test_add_edge():
    g = Graphs()
    node1 = g.add_node('niveen')
    node2 = g.add_node('smadi')
    g.add_Edge(node1,node2)
    assert  g.adjacency_list[node1][0].node == node2

def test_size_empty():
    graph = Graphs()
    assert 0 == graph.size()

def test_size():
    graph = Graphs()
    graph.add_node('niveen')
    assert  1 == graph.size()

def test_get_nodes():
    graph = Graphs()
    graph.add_node('niveen')
    graph.add_node('smadi')
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected


def test_get_Null():
    graph = Graphs()
    no = graph.get_nodes()
    assert no == "NULL"

def test_get_neighbors():
    graph = Graphs()
    niveen=graph.add_node('niveen')
    smadi=graph.add_node('smadi')
    graph.add_Edge(niveen, smadi, 10)
    neighbors = graph.get_neighbors(niveen)
    neighbor_edge = neighbors[0]


    assert neighbor_edge.node.value == 'smadi'
    assert neighbor_edge.weight == 10


def test_breadth_first_1():
    g=Graphs()
    a=g.add_node('a')
    b=g.add_node('b')
    c=g.add_node('c')

    g.add_Edge(a,b,5)
    g.add_Edge(b,c,4)  
    g.add_Edge(c,a,3)
    assert g.breadth_first(a)==['a', 'b', 'c']

def test_breadth_first_2():
    g=Graphs()
    a=g.add_node('a')
    b=g.add_node('b')
    c=g.add_node('c')
    d=g.add_node('d')
    e=g.add_node('e')

    g.add_Edge(a,b,5)
    g.add_Edge(a,c,4)  
    g.add_Edge(c,d,3)
    g.add_Edge(c,e,1)
    assert g.breadth_first(a)==['a', 'b', 'c','d','e']


def test_breadth_first_3():
    g=Graphs()
    a=g.add_node('Pandora')
    b=g.add_node('Arendelle')
    c=g.add_node('Metroville')
    d=g.add_node('Monstroplolis')
    e=g.add_node('Narnia')
    f=g.add_node('Naboo')
    g.add_Edge(a,b,5)
    g.add_Edge(b,c,4)  
    g.add_Edge(b,d,3)
    g.add_Edge(c,e,1)
    g.add_Edge(c,f,1)
    assert g.breadth_first(a)==['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']


def test_depth_first_search1():
    
    graph = {"A":["B","C", "D"],
           "B":["E"],
           "C":["F","G"],
           "D":["H"],
           "E":["I"],
           "F":["J"]}
    
    assert graph_depth_first(graph, "A") == "A D H C G F J B E I"   

def test_depth_first_search2():
    
    graph = {"A":["B","D"],
           "B":["C","D",],
           "C":["G"],
           "D":["E","H","F"],
           "H":["F"],
           }
    
    assert graph_depth_first(graph, "A") == "A D F H E B C G"

def test_depth_first_search3():
    
    graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
    
    assert graph_depth_first(graph, "5") == "5 7 8 3 4 2"
