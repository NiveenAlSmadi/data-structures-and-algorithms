from graph import __version__
from graph.graph import *

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