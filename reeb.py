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
    G = nx.Graph()
    for idx,node in enumerate(parent):
        if idx>0:
            G.add_edge(idx,node)
    
    plt.plot()
    nx.draw_networkx(G, font_weight='bold')
    return parent
    

