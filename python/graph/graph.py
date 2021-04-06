# AddNode()
# Adds a new node to the graph
# Takes in the value of that node
# Returns the added node
# AddEdge()
# Adds a new edge between two nodes in the graph
# Include the ability to have a “weight”
# Takes in the two nodes to be connected by the edge
# Both nodes should already be in the Graph
# GetNodes()
# Returns all of the nodes in the graph as a collection (set, list, or similar)
# GetNeighbors()
# Returns a collection of edges connected to the given node
# Takes in a given node
# Include the weight of the connection in the returned collection
# Size()
# Returns the total number of nodes in the graph

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """[Adds a new node to the graph
    Takes in the value of that node
    Returns the added node]
        """
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v
    
    def add_edge(self, start_vertex, end_vertex, weight=1):
        """[Adds a new edge between two nodes in the graph]
        """
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in Graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in graph')
        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)
        return edge
    
    def get_nodes(self):
        """[Returns all of the nodes in the graph as a collection (set, list, or similar)]
        """
        if len(self._adjacency_list) == 0:
            raise ValueError('Graph is Empty')

        return list(self._adjacency_list)

    
    def get_neighbors(self, v):
        """[Returns a collection of edges connected to the given node]
        """
        if v not in self._adjacency_list:
            raise KeyError('Vertex not in graph')
        return self._adjacency_list[v]
    
    def size(self):
        """[ Returns the total number of nodes in the graph]
        """
        if len(self._adjacency_list) == 0:
            raise ValueError('The graph is Empty')
        return len(self._adjacency_list)
   
class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight
