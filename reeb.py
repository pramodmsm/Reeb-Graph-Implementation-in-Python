import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pprint

from prompt_toolkit import prompt
from src.Undirected import Undirectedgraph,Utils
from copy import deepcopy

# function to build the reeb given the 2D scalar field/matrix              
def get_reeb(m,tree_type):
    g = Undirectedgraph(m,tree_type=tree_type)
    G = nx.Graph()
    processed_nodes = []
    
    # iterating over every node to build tree                                                             
    for node in g.m_flat:
        processed_nodes = g.build_tree(node,processed_nodes)
    
    processed_nodes = processed_nodes.pop()
    initial_g = deepcopy(g.graph)
    
    Utils.print(f'augmenting tree\n')
    g.augment(root=np.random.choice(processed_nodes,1)[0])
   
    return processed_nodes,initial_g,g.graph
    
    
if __name__ == "__main__":
    unit_size = int(input('enter unit size as (any integer > 0) :'))
    tree_type = str(input("enter type of tree 'merge/split' :"))
    debug_mode = str(input("enter debug mode 'yes/no' :"))
    Utils.verbose = True if debug_mode=='yes' else False
    scalar_field = np.random.choice(np.arange(1,np.square(unit_size)+3),size=(unit_size,unit_size),replace=False)
    Utils.print(f'input scalar field is\n\n {scalar_field}')
    
    if tree_type=='merge':
        _,merge_tree,aug_merge_tree = get_reeb(scalar_field,tree_type='merge')
        pprint.pprint('merge tree')
        pprint.pprint(merge_tree,compact=False,width=40)
        pprint.pprint('final reeb graph')
        pprint.pprint(aug_merge_tree,compact=False,width=40)
        Gm = nx.Graph(merge_tree)
        Gm_a = nx.Graph(aug_merge_tree)
    else:
        _,split_tree,aug_split_tree = get_reeb(scalar_field,tree_type='split')
        pprint.pprint('split tree')
        pprint.pprint(split_tree,compact=False,width=40)
        pprint.pprint('final reeb graph')
        pprint.pprint(aug_split_tree,compact=False,width=40)
        Gs = nx.Graph(split_tree)
        Gs_a = nx.Graph(aug_split_tree)

    # plots     
    plt.figure(figsize=(40,40))
    pprint.pprint('plotting visualizations')
    if tree_type=='merge':

        plt.subplot(121)
        nx.draw_networkx(Gm, font_weight='bold')
        plt.subplot(122)
        nx.draw_networkx(Gm_a, font_weight='bold')
    
    else:
        plt.subplot(121)
        nx.draw_networkx(Gs, font_weight='bold')
        plt.subplot(122)
        nx.draw_networkx(Gs_a, font_weight='bold')
    
    plt.show()

