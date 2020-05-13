from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # Build the edges in reverse
        graph.add_edge(pair[1], pair[0])

    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])

    max_path_len = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        # If the path is longer or equal and the value is smaller, or if the path is longer
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor