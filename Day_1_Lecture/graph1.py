class Graph:

    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()    # set of edges

    def add_edge(self, v1, v2):
        """ Add edge from v1 to v2. """

        # If they are both in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError("Vertex does not exist in graph!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertix_id):
        """ Breadth-first Traversal """
        
        q = Queue()
        q.enqueue(starting_vertix_id)
    
g = Graph()