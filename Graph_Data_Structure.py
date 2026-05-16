

def create_graph():
   
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['B', 'C']
    }
    return graph


def display_graph(graph):
    print("Graph Representation:")
    for vertex in graph:
        print(f"  {vertex} -> {graph[vertex]}")



def add_vertex(graph, vertex):

    if vertex not in graph:
        graph[vertex] = []
    else:
        print(f"  Vertex '{vertex}' already exists.")


def add_edge(graph, v1, v2):

    if v1 not in graph:
        add_vertex(graph, v1)
    if v2 not in graph:
        add_vertex(graph, v2)

    if v2 not in graph[v1]:
        graph[v1].append(v2)
    if v1 not in graph[v2]:
        graph[v2].append(v1)


def build_dynamic_graph():
   
    graph = {}

    for v in ['A', 'B', 'C', 'D']:
        add_vertex(graph, v)

    # Add edges
    add_edge(graph, 'A', 'B')
    add_edge(graph, 'A', 'C')
    add_edge(graph, 'B', 'D')

    return graph



def bfs(graph, start):
   
    visited = []          
    seen    = set()     
    queue   = deque()    

    queue.append(start)
    seen.add(start)

    while queue:
        vertex = queue.popleft()     
        visited.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)  

    return visited



def dfs(graph, start, visited=None):
    
    if visited is None:
        visited = []

    visited.append(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)   # recurse deeper

    return visited



def compare_bfs_dfs(graph, start):
    """
    Runs both BFS and DFS and prints a comparison table.
    """
    bfs_order = bfs(graph, start)
    dfs_order = dfs(graph, start)

    bfs_str = ' '.join(bfs_order)
    dfs_str = ' '.join(dfs_order)

    print("Comparison Table:")
    print("-" * 75)
    print(f"{'Algorithm':<12} {'Data Structure':<20} {'Traversal Order':<25} {'Suitable For'}")
    print("-" * 75)
    print(f"{'BFS':<12} {'Queue':<20} {bfs_str:<25} Shortest path in unweighted graph")
    print(f"{'DFS':<12} {'Stack / Recursion':<20} {dfs_str:<25} Exploring deep paths")
    print("-" * 75)



def bfs_shortest_path(graph, start, goal):

    queue = deque([[start]])
    seen  = set([start])

    while queue:
        path   = queue.popleft()
        vertex = path[-1]           

        if vertex == goal:
            return path             

        for neighbour in graph[vertex]:
            if neighbour not in seen:
                seen.add(neighbour)
                new_path = path + [neighbour]
                queue.append(new_path)

    return None   



def analyse_graph(graph):
    """
    Analyses the graph and prints:
    - Number of vertices
    - Number of edges
    - Degree of each vertex
    - Whether the graph is connected
    - Whether the graph is directed or undirected
    """
    num_vertices = len(graph)

    num_edges = sum(len(neighbours) for neighbours in graph.values()) // 2

    print(f"Number of vertices: {num_vertices}")
    print(f"Number of edges   : {num_edges}")

    print("Degree of each vertex:")
    for vertex in graph:
        print(f"  {vertex}: {len(graph[vertex])}")

    start      = next(iter(graph))
    reachable  = bfs(graph, start)
    connected  = len(reachable) == num_vertices

    print("The graph is connected." if connected else "The graph is NOT connected.")
    print("The graph is undirected.")


