from .graph import Graph

class Graph2Reeb(object):

    def __call__(self,g : Graph):
        root_nodes = []
        leaf_nodes = []


        for v in sorted(g.vertices):
            x = g.get_neighbours(v.index)
            m = list(filter(lambda a: a.index in x, leaf_nodes))
            print(v.index,list(map(lambda i: i.index,leaf_nodes)),list(map(lambda i: i.index,root_nodes)))
            # if v.index==6 : break
            if len(m)>0:    
                for n in m:
                    print(f'for {v.index} setting parent to {n.index}')
                    n.next = v
                    v.parent = n
                    leaf_nodes.remove(n)
                    if n.parent is None:
                        root_nodes.append(n)
                '''
                    look down upon to debug for larger matrix`
                '''
                for vertex in leaf_nodes:
                    if vertex.next is  v:
                        continue
                    tmp = vertex
                    while tmp is not None :
                        if tmp.index in x:
                            print(f'for {v.index} setting parent to {vertex.index}')
                            vertex.next = v
                            v.parent = vertex
                            leaf_nodes.remove(vertex)
                            break

                        tmp= tmp.parent       

                leaf_nodes.append(v)
            else:
                leaf_nodes.append(v)
        return leaf_nodes,root_nodes
