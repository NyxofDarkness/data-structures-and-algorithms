from python.graph.graph import Graph, Vertex, Edge

def breadth_first_traversal(self, s_node):
    visited = [False] * (max(Graph) + 1)

    queue = []

    queue.append(s_node)
    visited[s_node] = True

    while queue:

        s_node = queue.pop(0)
        print (s_node, end = " ")

        for i in self.graph[s_node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True