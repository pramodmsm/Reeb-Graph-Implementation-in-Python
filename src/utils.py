from .graph import Graph
from .vertex import Vertex

class MatrixToGraph(object):
    
    def __call__(self,m):
        g = Graph()

        [w, h] = m.shape

        for r in range(w):
            for c in range(h):
                v1 = m[r,c]
                g.add_vertex(Vertex(v1, r, c, 0))

                for i in [-1, 0, 1]:
                    if r + i < 0 or r + i >= h: continue
                    for j in [-1, 0, 1]:
                        if c + j < 0 or c + j >= w: continue
                        if i == j == 0: continue
                        v2 = m[r+i,c+j]
                        g.add_edge(v1, v2)

        return g