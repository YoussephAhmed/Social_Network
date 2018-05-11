from collections import defaultdict
from .models import Connection


def generate_graph(graph):
    graph_connections = Connection.objects.filter(status=1)

    for connection in graph_connections:
        graph.add_edge(connection.From, connection.To)


class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    #function to add edges
    def add_edge(self, u, v):
        self[u].append(v)

    #v is the starting node and u is the node we are trying to find a connection between it and v
    def explore(self,v, u, visited):
        visited[v] = True
        if v == u:
            return "connected"

        for i in self.graph[v]:
            if visited[i] == False:
                self.explore(self,i,visited)

    def DFS(self, v, u):
        visited = [False] * (len(self.graph))
        self.explore(v, u, visited)


