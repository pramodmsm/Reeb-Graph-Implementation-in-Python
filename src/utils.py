from .graph import Graph
from .vertex import Vertex
## data structures class

from audioop import reverse
from logging import raiseExceptions
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




class Stack(object):

    def __init__(self):
        self.stack = []
    
    def __len__(self):
        return len(self.stack)
    
    def __repr__(self):
        return self.stack

    def push(self,a : object):
        assert a is not None
        if type(a) == list:
            for i in a:
                self.stack.append(i)
        else:
            self.stack.append(a)
    
    def pop(self):
        return self.stack.pop(-1)

# node for a single and doubly linked list
class Node():

    def __init__(self,data):
        self.data = data
        self.next = None
        self.left = None
        self.right = None
        self.center = None
        
class Linked_list(Node):
        '''
            Class  for a Linked list
            Paramters
            Args :      nodes
            
            Returns  
            Linked list object with head pointer 
            data represented as shown below
            
            For e.g.:
            Linked_list(['a','b','c'])
            ==> 'a'->'b'->'c'->None  
        '''
        # initializes a linked list
        def __init__(self,nodes=None):
            self.head = None
            if nodes is not None:
                node = Node(data=nodes.pop(0))
                self.head = node
                for element in nodes:
                     node.next = Node(data=element)
                     node = node.next

        # length of a linked list
        def __len__(self):
            len=0
            for element in self:
                if element is not None:
                    len+=1
            return len

        # representative of a linked list     
        def __repr__(self):
            node = self.head
            nodes = []

            while node is not None:
                nodes.append(node.data)
                node = node.next
            nodes.append('None')
            return '->'.join(nodes)

        # traversal of linked list
        def __iter__(self):
            node = self.head
            while node is not None:
                yield node
                node = node.next

        # add a node at beginning of the linked list        
        def add_begin(self,node):
            node.next = self.head
            self.head = node

        # add a node at end of the linked list        
        def add_end(self,node):
            if self.head is None:
                self.head = node
                return
            for cur_node in self:
                pass
            cur_node.next = node
            node.next = None

        # add a node after any node of the linked list        
        def add_after(self,ref_node_data,new_node):
            if self.head is None:
               raise Exception('list empty')
            
            for node in self:
               if node.data == ref_node_data:
                    new_node.next = node.next
                    node.next = new_node
                    return
            raise Exception("reference node %s not found"%ref_node_data)
        
        # remove a node from linked list
        def remove(self,target_node_data):
            if self.head is None:
               raise Exception('list empty')

            if self.head.data == target_node_data:
                self.head = self.head.next
                return

            for node in self:
                if (node.next).data==target_node_data:
                    node.next = (node.next).next
                    return
            raise Exception("target node %s not found"%target_node_data)
             
        # reverse a linked list using pointers only
        def reverse(self):
            if self.head is None:
               raise Exception('list empty')

            previous = None
            current,following = self.head,self.head
            while current is not None:
                following = following.next
                following.next = current
                current.next = previous 
                previous = current
                current = following
            self.head = current
            return 
        
        # reverse a linked list using recursion 
        def reverse_s(self,node=None):
            if node is None:
                node = self.head
            if node.next is not None:
                self.reverse_s(node.next).next = node
                node.next = None
            else:
                self.head = node
            return node
                