from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # create graph
    ancestor_graph = Graph()
    # create path
    paths = []

    # add vertecies to graph
    for vertex in range(0, 20):
        ancestor_graph.add_vertex(vertex)

    # add edges to graph
    for ancestor in ancestors:
        ancestor_graph.add_edge(ancestor[0], ancestor[1])

    # add path to ancestor paths
    for vertex in ancestor_graph.vertices:
        if ancestor_graph.dfs(vertex, starting_node) is not None and len(ancestor_graph.dfs(vertex, starting_node)) > 0:
            paths.append(ancestor_graph.dfs(vertex, starting_node))

    if len(paths) == 1:
        return -1

    # find earliest neighbor
    start_path = paths[0]
    for path in paths:
        if len(path) > len(start_path) or len(path) == len(start_path) and path[0] < start_path[0]:
            start_path = path

    return start_path[0]