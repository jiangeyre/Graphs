class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
​
class Graph:
​
	def __init__(self):
		self.vertices = {}
​
	def add_vertex(self, vertex_id):
		self.vertices[vertex_id] = set()  # set of edges
​
	def add_edge(self, v1, v2):
		"""Add edge from v1 to v2."""
​
		# If they're both in the graph
		if v1 in self.vertices and v2 in self.vertices:
			self.vertices[v1].add(v2)
​
		else:
			raise IndexError("Vertex does not exist in graph")
​
	def get_neighbors(self, vertex_id):
		return self.vertices[vertex_id]
​
	def bft(self, starting_vertex_id):
		"""Breadth-first Traversal."""
​
		q = Queue()
		q.enqueue(starting_vertex_id)
​
		# Keep track of visited nodes
		visited = set()
​
		# Repeat until queue is empty
		while q.size() > 0:
			
			# Dequeue first vert
			v = q.dequeue()
​
			# If it's not visited:
			if v not in visited:
				print(v)
​
				# Mark visited
				visited.add(v)
​
				for next_vert in self.get_neighbors(v):
					q.enqueue(next_vert)
​
	def dft_recursive(self, start_vert, visited=None):
		print(start_vert)
​
		if visited is None:
			visited = set()
​
		visited.add(start_vert)
​
		for child_vert in self.vertices[start_vert]:
			if child_vert not in visited:
				self.dft_recursive(child_vert, visited)
​
	def dfs_recursive(self, start_vert, target_value, visited=None, path=None):
		print(start_vert)
​
		if visited is None:
			visited = set()
​
		if path is None:
			path = []
​
		visited.add(start_vert)
​
		# Make a copy of the list, adding the new vert on
		path = path + [start_vert]
​
		# Base case
		if start_vert == target_value:
			return path
​
		for child_vert in self.vertices[start_vert]:
			if child_vert not in visited:
				new_path = self.dfs_recursive(child_vert, target_value, visited, path)
				
				if new_path:
					return new_path
​
		return None
​
g = Graph()
g.add_vertex(99)
g.add_vertex(3)
g.add_vertex(3490)
g.add_vertex(34902)
g.add_edge(99, 3490)   # Connect node 99 to node 3490
g.add_edge(99, 3)      # Connect node 99 to node 3
g.add_edge(3, 99)      # Connect node 3 to node 99
g.add_edge(3490, 34902)
​
​
#print(g.get_neighbors(99))
#print(g.get_neighbors(3))
​
g.bft(99)
g.bft(3490)
​
g.dft_recursive(99)
print(g.dfs_recursive(99, 34902))