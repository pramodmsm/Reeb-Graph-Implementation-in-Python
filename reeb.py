from prompt_toolkit import prompt
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
    input_matrix =  np.array([
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
    unit_size = int(input("enter matrix size as integer"))
    scalar_field = np.random.choice(np.arange(1,np.square(unit_size)+1),size=(unit_size,unit_size),replace=False)
    print(f'input scalar field is\n\n {scalar_field}')
    
    parent = get_reeb(scalar_field)
    G = nx.Graph()
    for idx,node in enumerate(parent):
        if idx>0:
            G.add_edge(idx,node)
    
    nx.draw_networkx(G, font_weight='bold')
    plt.show()