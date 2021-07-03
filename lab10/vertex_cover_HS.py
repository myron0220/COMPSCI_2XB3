import random

# Vertex cover. (Minimum vertex cover)
# Find the set of vertcies to cover all edges
# We implemented it with undirected and unweighted graph
class Graph:

    def __init__(self):
        self.adj = {}

    def are_connected(self, node1, node2):
        for node in self.adj[node1]:
            if node == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def remove_edge(self, node1, node2):
        if node2 in self.adj[node1]:                    
            self.adj[node1].remove(node2)
        if node1 in self.adj[node2]:                    
            self.adj[node2].remove(node1)

    def remove_incident_edges(self, node):      
        for neighbour in self.adj[node]:
            self.adj[neighbour].remove(node)
        self.adj[node] = []

    def has_no_edges(self):
        for node in self.adj:                   # self.adj = {0:[1,2,3], 1:[0,2], 2:[0,1], 3:[0]}
            if len(self.adj[node]) > 0:
                return False
        return True

    def copy(self):
        new_G = Graph()
        new_G.adj = self.adj.copy()
        for node in self.adj:
            new_G.adj[node] = self.adj[node].copy()
        return new_G

    def number_of_nodes(self):
        return len(self.adj)


## Vertex cover implementation
def vertex_cover(G):                            # G.adj = {0:[1,2,3], 1:[0,2], 2:[0,1], 3:[0]}
    nodes = G.adj.keys()                        # nodes = [0, 1, 2, 3]
    best_cover = nodes                          # best_covers = [0, 1, 2, 3]    
    covers = power_set(nodes)                   # covers = power_set(nodes) = [[], [1], ... , [0, 1, 2, 3]]
    for cover in covers:                         
        if is_vertex_cover(G, cover):           # Decide if cover is a vertex_cover
            if len(cover) < len(best_cover):     
                best_cover = cover
    return best_cover                           # Minumum vertex_cover

def is_vertex_cover(G, cover):                  # if is_vertex_cover(G, [0])
    temp_G = G.copy()                           # temp_G = {0:[1,2,3], 1:[0,2], 2:[0,1], 3:[0]}
    for node in cover:
        temp_G.remove_incident_edges(node)      # temp_G.remove_incident_edges(0)
    if temp_G.has_no_edges():                   # if temp_G.has_no_edges() true means, "cover" is a vertex_cover 
        return True
    return False

def power_set(elements):
    if elements == []:
        return [[]]
    return add_to_each(power_set(elements[1:]), elements[0]) + power_set(elements[1:])
    # power_set([1, 2, 3]) = add_to_each(power_set([2, 3]), 1) + power_set([2, 3]) -- a
    #     in a -> power_set([2, 3]) = add_to_each(power_set([3]), 2) + power_set([3]) -- b
    #         in b -> power_set([3]) = add_to_each(power_set([]), 3) + power_set([]) -- c
    #             in c -> power_set([]) = [[]]
    #             in c -> add_to_each([[]], 3) = [[3]]
    #         in b -> power_set([3]) = [[3]] + [[]] = [[3], []]
    #     in a -> power_set([2, 3]) = add_to_each([[3], []], 2) + [[3], []] 
    #          -> power_set([2, 3]) = [[3, 2], [2]] + [[3], []] 
    #          -> power_set([2, 3]) = [[3, 2], [2], [3], []]
    # power_set([1, 2, 3]) = add_to_each([[3, 2], [2], [3], []], 1) + [[3, 2], [2], [3], []]
    #                      = [[3, 2, 1], [2, 1], [3, 1], [1]] + [[3, 2], [2], [3], []]
    #                      = [[3, 2, 1], [2, 1], [3, 1], [1], [3, 2], [2], [3], []]

def add_to_each(sets, element):
    my_sets = sets.copy()
    for my_set in my_sets:
        my_set.append(element)
    return my_sets

def create_random_graph(n, m):
    G = Graph()
    for i in range(n):
        G.add_node(i)
    edges = create_edge_list(n)
    for _ in range(m):
        edge = random.choice(edges)
        edges.remove(edge)
        G.add_edge(edge[0],edge[1])
    return G

def create_edge_list(n):
    edges = []
    for i in range(n):
        for j in range(i+1,n):
            edges.append((i,j))
    return edges


# Independent set  
# Independent set is a subset of the vertex set of a graph that contains no pair of adjacent vertices
# Maximal, maximum independent sets (Not unique)
# Vertices - maximum independent sets = Minumum vertex cover

# Clique
# Clique is a subset of the vertex set of a graph that is a complete graph. (Each vertes is connected to all other vertices)