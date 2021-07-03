import disjoint_set
import min_heap

class WeightedGraph:

    def __init__(self):                         # G = WeightedGraph(), G.add_node(0..3), G.add_edge(0..3, 10..40)
        self.adj = {}                           # G.adj = {0:[1,2], 1:[0,2], 2:[0,1], 3:[0]}
        self.weights = {}                       # G.weight = {(0,1):10, (1,0):10, 
                                                #      (1,2):20, (2,1):20, (0,2):40, (2,0):40, (0,3):30, (3,0):30}

    def are_connected(self, node1, node2):      
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if not self.are_connected(node1, node2):
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
        self.weights[(node1, node2)] = weight
        self.weights[(node2, node1)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)

"""
MST is a spanning path makes samllest sum of edge weights
## @brief Find a undirected-weighted graph's MST(undirected-weighted graph) with kruskal algorithm.
#  @detail Implement kruskal algorithm with disjoint_set(Union-find) data structure.
#          The disjoint_set(Union-find) is used to determine whether to use the minimum edge.
#          Minimum priority queue of edges is implemented by a min_heap data sturcuture.   
"""
def kruskal(G):             # G.adj = {0:[1,2,3], 1:[0,2], 2:[0,1], 3:[0]}
                            # G.weight = {(0,1):10, (1,2):20, (0,2):40, (0,3):30}
    MST = WeightedGraph()   # MST = {}
    nodes = []              # nodes = []
    for node in G.adj:
        MST.add_node(node)  # MST = {0:[], 1:[], 2:[], 3:[]}
        nodes.append(node)  # nodes = [0, 1, 2, 3]
    ds = disjoint_set.DisjointSet(nodes)    # ds.parents = {0:0, 1:1, 2:2, 3:3}, ds.size = {0:1, 1:1, 2:1, 3:1}
    Q = min_heap.MinHeap([])                # Q = []
    for node in G.adj:                      # G.adj = {0:[1,2,3], 1:[0,2], 2:[0,1], 3:[0]}
        for neighbour in G.adj[node]:
            Q.insert(min_heap.Element((node, neighbour), G.w(node, neighbour)))
            # Q.insert(min_heap.Element((0, 1), G.w(0,1)))
            # Q.insert(min_heap.Element((0, 2), G.w(0,2)))
            # Q.insert(min_heap.Element((0, 3), G.w(0,3)))
            # Q.insert(min_heap.Element((1, 0), G.w(1,0)))
            # Q.insert(min_heap.Element((1, 2), G.w(1,2))) ...
            ## Min HeapSort based on weights
    print("Q: ", Q)
            # Q:                  ((0, 1),10) 
            #         ((1, 0),10)         ((2, 1),20)
            #     ((3, 0),30)     ((1, 2),20)     ((0, 3),30)     ((2, 0),40)
            #   ((0, 2),40)    
    print("ds: ", ds)
            # ds:  [[0], [1], [2], [3]]
            # ds.parents = {0:0, 1:1, 2:2, 3:3}
            # ds.size = {0:1, 1:1, 2:1, 3:1}
    while not Q.is_empty():
        current_edge = Q.extract_min().value
        print("Considering edge: " + str(current_edge) + str(G.w(current_edge[0], current_edge[1])))
        if ds.find(current_edge[0]) != ds.find(current_edge[1]):
            MST.add_edge(current_edge[0], current_edge[1], G.w(current_edge[0], current_edge[1]))
            ds.union(current_edge[0], current_edge[1])
            print("ds: ", ds)
            print("ds.parents: ", ds.parents)
            # CYCLE1
            # ds:  [[0, 1], [2], [3]]
            # ds.parents:  {0: 0, 1: 0, 2: 2, 3: 3}
            # CYCLE2
            # ds:  [[0, 1, 2], [3]]
            # ds.parents:  {0: 0, 1: 0, 2: 0, 3: 3}
            # CYCLE3
            # ds:  [[0, 1, 2, 3]]
            # ds.parents:  {0: 0, 1: 0, 2: 0, 3: 0}
        print(MST.adj)
    return MST                 # MST = {0:[1,3], 1:[0,2], 2:[1], 3:[0]}










# G = WeightedGraph()
# G.add_node("a")
# G.add_node("b")
# G.add_node("c")
# G.add_node("d")
# G.add_node("e")
# G.add_node("f")
# G.add_node("g")

# G.add_edge("a", "f", 2)
# G.add_edge("a", "b", 2)
# G.add_edge("a", "d", 7)
# G.add_edge("b", "f", 5)
# G.add_edge("b", "d", 4)
# G.add_edge("b", "c", 1)
# G.add_edge("b", "e", 3)
# G.add_edge("c", "f", 4)
# G.add_edge("c", "e", 4)
# G.add_edge("d", "e", 1)
# G.add_edge("d", "g", 5)
# G.add_edge("e", "g", 7)


# G.adj = {0:[1,2], 1:[0,2], 2:[0,1], 3:[0]}
# G.weight = {(0,1):10, (1,2):20, (0,2):40, (0,3):30}
G = WeightedGraph()
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)

G.add_edge(0,1,10)
G.add_edge(1,2,20)
G.add_edge(0,2,40)
G.add_edge(0,3,30)

gk = kruskal(G)
print(G.adj)
print(gk.adj)
print(gk.weights)

# MST = {0:[1,3], 1:[0,2], 2:[1]}









"""
def kruskal(G):
    MST = WeightedGraph()
    nodes = []
    for node in G.adj:
        MST.add_node(node)
        nodes.append(node)
    ds = disjoint_set.DisjointSet(nodes)
    Q = min_heap.MinHeap([])
    for node in G.adj:
        for neighbour in G.adj[node]:
            Q.insert(min_heap.Element((node, neighbour), G.w(node, neighbour)))
    print(ds)
    while not Q.is_empty():
        current_edge = Q.extract_min().value
        if ds.find(current_edge[0]) != ds.find(current_edge[1]):
            MST.add_edge(current_edge[0], current_edge[1], G.w(current_edge[0], current_edge[1]))
            ds.union(current_edge[0], current_edge[1])
            print(ds)
    return MST
"""