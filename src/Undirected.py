# class for building a tree given a scalar field to obtain an augmented join tree

from tabnanny import verbose
from pipe import where,select,traverse,dedup
from collections import defaultdict
from copy import deepcopy
from src.utils import Stack

class Utils(object):
	verbose: bool = True
	r"""A global boolean property to specify if the wrapper must print contents or
	not."""

	@staticmethod
	def print(*args, **kwargs):

		if 'flush' not in kwargs:
			kwargs['flush'] = True

		if kwargs.get('verbose', Utils.verbose):
			# del kwargs['verbose']
			print(*args, **kwargs)



class Undirectedgraph:
	'''
		Purpose
			This class constructs an undirected graph from a given 2D scalar field
		
		Args
			m			:	input 2D scalar field/integer matrix
			tree_type 	:	merge/split (optional)
							if tree_type == 'merge' --> nodes are processed in ascending 
							order
							if tree_type == 'split' --> nodes are processed in descending
							order
	'''		
	
	def __init__(self,m,tree_type='merge'):
		self.graph = defaultdict(list) # default dictionary to store graph
		self.m = m
		self.min = m.min()
		self.max = m.max()
		self.tree_type = tree_type
		self.m_flat = self.m.flatten()
		self.m_flat.sort()
		if self.tree_type == 'split':
			self.m_flat = np.flip(self.m_flat)
		Utils.print(self.m_flat)
	
	# reprenstation of a graph
	def __repr__(self) -> dict:
		return self.graph
	
	# degree of a node 
	def degree(self,node) -> int:
		return len(self.graph[node])
	
	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)
		
	# method to delete a node and its connected edges
	def delete(self,n):
		list(self.graph[n] | select(lambda x:self.graph[x].remove(n)))
		del(self.graph[n])
	
	# get adjacent neighbours of a node in tree 
	def get_neighbours(self,node):
		return self.graph[node]
	
	# utility to get indices of element in the 2D scalar field
	def get_index(self, item):
		[x, y] = np.where(self.m == item)
		x, y = x[0], y[0]
		return x, y
	
	# utility to check if any of the elements are neighbours to node
	def is_neighbour(self,elements,node):
		[r, c] = self.m.shape
		[x, y] = self.get_index(node)

		for element in elements:
			if element in self.m[max(0,x-1):min(x+2,r), max(y-1,0):min(y+2, c)]:
				return True
		
		return False
    
	# utility to merge connected components
	def merge_sets(self,sets,node):
		con_com = {node:[],-1:[]}
		Utils.print(f'before merging processed_nodes: {sets}')
		for subset in sets:
			if node in subset:
				con_com[node].append(subset)
				con_com[node] = list(con_com[node] | traverse | dedup)
			else:
				con_com[-1].append(subset)

		sets = [con_com[node]]
		if len(con_com[-1])!= 0:
			for i in con_com[-1]: sets.append(i)
		con_com.clear()
		Utils.print(f'post merging processed_nodes: {sets}')
		return sets
	
	# main function to build either trees passing single node to given tree
	def build_tree(self,node,processed_nodes):
		'''
			Args
				node			:	a new node to be added to build the tree
				processed_nodes	:	set of nodes already part of the tree/processed 
			
			Purpose
				build the tree by adding every node based on neighbourhood in scalar field
				and connecting components/nodes
			
			Example
				input scalar field is
							   [[ 1 21  8 25 27]
								[ 7 16 24 23  5]
								[ 2  4  9 18 11]
								[13 20 26 10 22]
								[ 6 17 12 15 14]]
				processed_nodes=[]
				
				subset [1] from processed nodes [[1]], node is 2
				is node 2 a neighbour of subset[1] : False

				subset [1] from processed nodes [[1], [2]], node is 4
				is node 4 a neighbour of subset[1]: False

				subset [2] from processed nodes [[1], [2]], node is 4
				is node 4 a neighbour of subset[2]: True
				appending node 4 to processed_nodes [[1], [2]]
				before merging processed_nodes[[1], [2, 4]]
				post merging processed_nodes[[2, 4], [1]]
				...
		'''
		flag_no_neigbhour = True
		if len(processed_nodes)!=0:
			for idx,subset in enumerate(processed_nodes):
				
				Utils.print(f'\nsubset {subset} from processed nodes {processed_nodes}, node is {node}')
				Utils.print(f'is node {node} a neighbour of subset {subset}: {self.is_neighbour(subset,node)}')
				
				if self.is_neighbour(subset,node):
					if self.tree_type == 'merge':
						self.addEdge(np.max(subset),node)
					else:
						self.addEdge(np.min(subset),node)
					Utils.print(f'merging node {node} to subset {subset} in processed_nodes')
				
					processed_nodes[idx].append(node)
					flag_no_neigbhour = False

			if flag_no_neigbhour:
				processed_nodes.append([node])
			else:
				processed_nodes = self.merge_sets(processed_nodes,node)
		else:
			processed_nodes.append([node])
		return processed_nodes
		
	
	# optimized iterative algorithm 
	def augment(self,root: int):
		'''
		Args
			root:any node in graph 

		Purpose
			Iterative method of Graph augmentation of graph retaining only critical nodes(a.k.a saddle points)
			and root nodes reducing the size of graph considerably

		Output
			returns: None

		time complexity: O(n^2)
		Space complexity: O(n)
		'''
		to_visit=[]
		to_visit.append(root)
		counter=0
		
		while(counter<len(to_visit)):
			node=to_visit[counter]
			neighbours=self.get_neighbours(node)
			if self.degree(node)==2:
				self.addEdge(neighbours[0],neighbours[1])
				self.delete(node)
			to_visit=to_visit+list(neighbours | where(lambda x: x not in to_visit))
			counter+=1

		del(to_visit)
		del(counter)
