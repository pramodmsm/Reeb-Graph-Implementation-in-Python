from prompt_toolkit import prompt
from src.Undirected import Undirectedgraph,Utils

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

              
def get_reeb(m,tree_type):
    g = Undirectedgraph(m,tree_type=tree_type)
    G = nx.Graph()
    processed_nodes = []
                                                                                 # O(n)  space complexity
    for node in g.m_flat:
        processed_nodes = g.build_tree(node,processed_nodes)
    
    return processed_nodes,g
    
if __name__ == "__main__":
    Utils.verbose = True
    unit_size = int(input('enter unit size as integer :'))
    # tree_type = str(input("enter type of tree 'merge/split' :"))
    scalar_field = np.random.choice(np.arange(1,np.square(unit_size)+1),size=(unit_size,unit_size),replace=False)
    Utils.print(f'input scalar field is\n\n {scalar_field}')
    
    _,merge_tree = get_reeb(scalar_field,tree_type='merge')
    _,split_tree = get_reeb(scalar_field,tree_type='split')
    Gm = nx.Graph(merge_tree.graph)
    Gs = nx.Graph(split_tree.graph)
    Utils.print([merge_tree.graph])
    plt.figure(figsize=(20,20))
    plt.subplot(121)
    nx.draw_networkx(Gm, font_weight='bold')
    plt.subplot(122)
    nx.draw_networkx(Gs, font_weight='bold')
    plt.show()