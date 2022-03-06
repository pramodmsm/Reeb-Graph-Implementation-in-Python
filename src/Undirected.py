from collections import defaultdict
from tabnanny import verbose
import numpy as np
from pipe import where,select,traverse,dedup
#This class represents a undirected graph using adjacency processed_nodes representation

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

	def __init__(self,m,tree_type='merge'):
		self.graph = defaultdict(list) # default dictionary to store graph
		self.m = m
		self.tree_type = tree_type
		self.m_flat = self.m.flatten()
		self.m_flat.sort()
		if self.tree_type == 'split':
			self.m_flat = np.flip(self.m_flat)
		Utils.print(self.m_flat)
	
	def __repr__(self) -> dict:
		return self.graph
	
	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	# function to check an edge in graph given nodes (u,v)
	def isEdge(self,u,v):
		if u<v and v in self.graph[u] :
			return True
		return False

	# get adjacent neighbours of a node in tree 
	def get_neighbours(self,node):
		return self.graph[node]
	
	# A utility function to find the root parent of an element i
	def find_parent(self, parent,i):
		if parent[i] == -1:
			return i
		if parent[i]!= -1:
			return self.find_parent(parent,parent[i])

	# A utility function to do union of two subsets
	def union(self,parent,x,y):
		parent[x] = y


	def get_index(self, item):
		[x, y] = np.where(self.m == item)
		x, y = x[0], y[0]
		return x, y
	
	def is_neighbour(self,children,node):
		[r, c] = self.m.shape
		[x, y] = self.get_index(node)

		for child in children:
			if child in self.m[max(0,x-1):min(x+2,r), max(y-1,0):min(y+2, c)]:
				return True
		
		return False
    
	def merge_sets(self,sets,node):
		con_com = {node:[],-1:[]}
		# Utils.print(f'before merging processed_nodes{sets}')
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
		Utils.print(f'post merging processed_nodes{sets}')
		return sets

	def build_tree(self,node,processed_nodes):
		flag_no_neigbhour = True
		if len(processed_nodes)!=0:
			for idx,subset in enumerate(processed_nodes):
				Utils.print(f'\nsubset {subset} from processed nodes {processed_nodes}, node is {node}')
				Utils.print(f'is node {node} a neighbour of subset{subset}{self.is_neighbour(subset,node)}')
				if self.is_neighbour(subset,node):
					if self.tree_type == 'merge':
						self.addEdge(np.max(subset),node)
					else:
						self.addEdge(np.min(subset),node)
					Utils.print(f'appending node {node} to processed_nodes {processed_nodes}')
					processed_nodes[idx].append(node)
					flag_no_neigbhour = False

			if flag_no_neigbhour:
				processed_nodes.append([node])
			else:
				processed_nodes = self.merge_sets(processed_nodes,node)
		else:
			processed_nodes.append([node])
		return processed_nodes