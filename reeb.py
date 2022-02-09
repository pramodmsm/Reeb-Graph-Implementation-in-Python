from src.Undirected import Undirectedgraph

import numpy as np
from pipe import traverse
import networkx as nx
import matplotlib.pyplot as plt

def get_reeb(m):
    g = Undirectedgraph(m)
    G = nx.Graph()
    processed_nodes = []
    parent = [-1]*(len(g.m_flat)+1)                                             # O(n)  space complexity

    for node in g.m_flat:
        processed_nodes,parent = g.check_for_parents(node,processed_nodes,parent)
    
    parent = parent[:-1]
   
    return parent
    
if __name__ == "__main__":
    input_matrix = np.array([
    [1, 6, 3],
    [2, 7, 4],
    [5, 8, 9]
                            ])
    input_matrix =  np.array([
    [1,7,12,13],
    [9,2,6,5 ],
    [14,8,11,10],
    [15,16,4,3]
                            ])
    input_matrix = np.random.choice(np.arange(1,17),size=(4,4),replace=False)
    parent = get_reeb(input_matrix)
    G = nx.Graph()
    for idx,node in enumerate(parent):
        if idx>0:
            G.add_edge(idx,node)
    
    plt.plot()
    nx.draw_networkx(G, font_weight='bold')
    plt.show()