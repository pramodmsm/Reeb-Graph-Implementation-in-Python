from prompt_toolkit import prompt
from src.Undirected import Undirectedgraph

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def get_reeb(m):
    g = Undirectedgraph(m)
    G = nx.Graph()
    processed_nodes = []
                                                # O(n)  space complexity
    for node in g.m_flat:
        processed_nodes = g.check_for_parents(node,processed_nodes)
    
    return processed_nodes,g
    
if __name__ == "__main__":
    unit_size = int(input("enter matrix size as integer"))
    scalar_field = np.random.choice(np.arange(1,np.square(unit_size)+5),size=(unit_size,unit_size),replace=False)
    print(f'input scalar field is\n\n {scalar_field}')
    
    processed_nodes,g = get_reeb(scalar_field)
    G = nx.Graph(g.graph)
    nx.draw_networkx(G, font_weight='bold')
    plt.show()