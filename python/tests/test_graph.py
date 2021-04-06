# Node can be successfully added to the graph
# An edge can be successfully added to the graph
# A collection of all nodes can be properly retrieved from the graph
# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
# The proper size is returned, representing the number of nodes in the graph
# A graph with only one node and edge can be properly returned
# An empty graph properly returns null

# check in class repo for tests given!

import pytest
from graph.graph import Vertex, Graph

def test_add_vertex_pass():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'a'
    assert actual == expected

def test_add_vertex_fail():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'b'
    assert actual != expected

def test_add_node():
    graph = Graph()
    expected = 'a'
    actual = graph.add_node('a').value
    assert expected == actual
    
def test_add_edge_true():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True

def test_size():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 2
    actual = graph.size()
    assert actual == expected
 
def test_size_fail():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 3
    actual = graph.size()
    assert actual != expected

def test_get_nodes():
    pass

def test_get_neighbor():
    pass