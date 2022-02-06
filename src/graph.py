from .vertex import Vertex

# Class 
class Graph(object):

    ''' A simple graph object defined by vertices and edges
    '''

    def __init__(self):
        self.vertices = []
        self.adjacency = dict()

    def add_vertex(self,v: Vertex):
        
        if v not in self.vertices:
            self.vertices.append(v)
            if v not in self.adjacency:
                self.adjacency[v.index] = []

    def remove_vertex(self,v:Vertex):
        if v in self.vertices:
            self.vertices.remove(v)
    
    def add_edge(self,v:int,w:int):
        if w not in self.adjacency[v]:
            # append to list in the dictionary as per key
            self.adjacency[v].append(w)

    def get_neighbours(self, v: int):
        return self.adjacency.get(v, [])
