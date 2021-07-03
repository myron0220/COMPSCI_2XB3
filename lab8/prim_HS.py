import random
import min_heap
import timeit
import copy

#Undirected graph using an adjacency list
class WeightedGraph:

    def __init__(self, n):                          # G = WeightedGraph(4)
        self.adj = {}                               # {0:[], 1:[], 2:[], 3:[]}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        for edge in self.adj[node1]:
            if edge[0] == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2, weight):       # G.add_edge(0..3, 10..40)
        for info in self.adj[node2]:
            if node1 == info[0]:
                return
        self.adj[node1].append((node2, weight))
        self.adj[node2].append((node1, weight))     # G.adj = {0:[(1,10),(2,40),(3,30)], 1:[(0,10),(2,20)], 2:[(1,20),(0,40)], 3:[(1,30)]}

    def w(self, node1, node2):
        for edge_info in self.adj[node1]:
            if node2 == edge_info[0]:
                return edge_info[1]

    def number_of_nodes(self):
        return len(self.adj)

    def copy(self):
        G = WeightedGraph(self.number_of_nodes())
        for node in self.adj:
            G.adj[node] = self.adj[node].copy()
        return G

"""
MST is a spanning path makes samllest sum of edge weights
## @brief Find a undirected-weighted graph's MST(undirected-weighted graph) with prim's algorithm.
#  @detail 
# 
#   
"""
def create_random_complete_graph(n,upper):
    G = WeightedGraph(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G

# G.adj = {0:[(1,10),(2,40),(3,30)], 1:[(0,10),(2,20)], 2:[(1,20),(0,40)], 3:[(1,30)]}
def graph_weight(G):
    total = 0
    for node in G.adj:                           # node = [0..3]
        # G.adj[node] = [(1,10),(2,40),(3,30)] , [(0,10),(2,20)] .. 
        for info in G.adj[node]:                 
            total += G.w(node, info[0])
    return total/2

def prim1(G):                                    
    MST = WeightedGraph(G.number_of_nodes())        # MST = {0:[], 1:[], 2:[], 3:[]}
    marked = {}                                     
    for i in range(G.number_of_nodes()):
        marked[i] = False                           # marked = {0:False, 1:False, 2:False, 3:False}
    marked[0] = True
    for _ in range(G.number_of_nodes() - 1):        # #Cylce = #nodes(V) - 1
        current_weight = 99999
        # Based on the unmarked vertices, find the minimum edge(weight) to the marked vertice and add the edge to MST.
        # Repeat the process V-1 times. 
        # G.adj = {0:[(1,10),(2,40),(3,30)], 1:[(0,10),(2,20)], 2:[(1,20),(0,40)], 3:[(0,30)]}
        for node in G.adj:                          # node = [0..3] 
            if not marked[node]:
                # G.adj[node] = [(1,10),(2,40),(3,30)] , [(0,10),(2,20)] , [(1,20),(0,40)] , [(0,30)]
                for info in G.adj[node]:
                    neighbour = info[0]
                    weight = info[1]
                    if weight < current_weight and marked[neighbour]:
                        current_weight = weight
                        current_source, current_destination = node, neighbour
        MST.add_edge(current_source, current_destination, current_weight)
        marked[current_source] = True
    return MST          # MST = {0: [(1, 10), (3, 30)], 1: [(0, 10), (2, 20)], 2: [(1, 20)], 3: [(0, 30)]}
  

def prim2(G):
    MST = WeightedGraph(G.number_of_nodes())
    marked = {}
    pred = {}
    for i in range(G.number_of_nodes()):
        marked[0] = False
    Q = min_heap.MinHeap([])
    for i in range(1, G.number_of_nodes()):
        Q.insert(min_heap.Element(i, 9999))
    Q.insert(min_heap.Element(0,0))
    while not Q.is_empty():
        v = Q.extract_min().value
        if v != 0:
            MST.add_edge(v, pred[v], G.w(v,pred[v]))
        marked[v] = True
        for edge_info in G.adj[v]:
            if edge_info[0] in Q.map:
                if edge_info[1] < Q.get_element_from_value(edge_info[0]).key: 
                    Q.decrease_key(edge_info[0], edge_info[1])
                    pred[edge_info[0]] = v
    return MST

# def time_test(n, runs, prim):
#     total = 0
#     for _ in range(runs):
#         G = create_random_complete_graph(n, 100)
#         start = timeit.default_timer()
#         prim(G)
#         total += timeit.default_timer() - start
#     return total/runs

"""
## @brief Time_test
#  @detail prim1 time_complexity is O(VE), prime2 is O(--)
"""
# G = WeightedGraph(4)
# G.add_edge(0,1,10)
# G.add_edge(1,2,20)
# G.add_edge(0,2,40)
# G.add_edge(0,3,30)

# print(G.adj)
# prim1 = prim1(G)
# print(prim1.adj)

def time_test(runs, prim, Graph):
    total = 0
    for _ in range(runs):
        G = Graph.copy()
        start = timeit.default_timer()
        prim(G)
        total += timeit.default_timer() - start
    return total/runs

# G = create_random_complete_graph(30, 100)
# t1 = time_test(30, prim1, G)
# t2 = time_test(30, prim2, G)
# (t1-t2)/t2*100  
