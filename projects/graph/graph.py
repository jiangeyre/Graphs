"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # If they are both in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError("Vertex does not exist in graph!")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        # Keep track of visited nodes
        visited = set()

        # Repeat until queue is empty
        while q.size() > 0:
            # Dequeue first vertex
            v = q.dequeue()

            # If not visited
            if v not in visited:
                print(v)

                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push the starting vertex id
        s = Stack()
        s.push(starting_vertex)
        # create a set to store a visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for visualization)
                print(v)
                visited.add(v)
                # add all neighbors to the top of stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
            
        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.vertices[starting_vertex]:
            if v not in visited:
                self.dft_recursive(v, visited)

        return



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print("This is breadth-first search.")

        q = Queue()
        # enqueue path to the starting vertex
        q.enqueue([starting_vertex])
        # create a set to track vertices we have visited
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path
            current_path = q.dequeue()
            # get last vertex from the path
            last_vertex = current_path[-1]
            # if vertex has not been visited:
            if last_vertex not in visited:
                # check the destination
                if last_vertex == destination_vertex:
                    return current_path
                # mark is as visited
                visited.add(last_vertex)
                # add a path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:
                    # clone path
                    new_path = [*current_path]
                # add neighbor to the back of the queue
                    new_path.append(v)
                    q.enqueue(new_path)
                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print("This is depth-first search.")

        # create an empty stack
        stack = Stack()
        # push the starting_vertex id onto the stack
        stack.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty
        while stack.size() > 0:
            # dequeue the first path
            current_path = stack.pop()
            # get the last vertex from the path
            last_vertex = current_path[-1]
            # it has not been visited:
            if last_vertex not in visited:
                # check destination
                if last_vertex == destination_vertex:
                    return current_path
                # mark it as visited
                visited.add(last_vertex)
                # add path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:

                    # clone path
                    new_path = [*current_path]

                # add neighbor to the back of the queue
                    new_path.append(v)
                    stack.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex, path=Stack(), visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print("This is DFS using recursion.")

        visited = set()

        c_path = path.pop()

        if c_path is None:
            c_path = [starting_vertex]
        
        if c_path[-1] not in visited:
            visited.add(c_path[-1])

            for nay in self.get_neighbors(c_path[-1]):
                if nay == destination_vertex:
                    c_path.append(nay)

                    return c_path
                
                c_path_copy = c_path.copy()
                c_path_copy.append(nay)

                path.push(c_path_copy)
            
            return self.dfs_recursive(starting_vertex, destination_vertex, path, visited)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
