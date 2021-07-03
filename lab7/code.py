import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
import random
from graphs import *


# Randomly construct an undirected graph.
# Pass True to is_plot if want illustration.
def cons_random_graph(k, c, is_plot):
    V = set([v for v in range(k)])
    E = set()
    # G is our graph.
    G = Graph(k)
    for combination in random.sample(list(combinations(V, 2)), c):
        (node1, node2) = combination
        G.add_edge(node1, node2)
        E.add(combination)
    # use network for illustration
    net_graph = nx.Graph()
    net_graph.add_nodes_from(V)
    net_graph.add_edges_from(E)
    if is_plot:
        pos = nx.spring_layout(net_graph)
        nx.draw_networkx(net_graph, pos)
        plt.title("Random graph with " + str(k) + " nodes and " + str(c) + " edges")
        plt.show()
    return G

# Calculate portion of graphs which have a circle.
# n random times
# k # of nodes
# c # of edges
def get_portion_cycle(n, k, c):
    num_of_cyclic_graph = 0
    for _ in range(n):
        if (has_cycle(cons_random_graph(k, c, False))):
            num_of_cyclic_graph += 1
    portion = num_of_cyclic_graph / n
    return portion

def get_portion_connected(n, k, c):
    num_of_connected_graph = 0
    for _ in range(n):
        if (is_connected(cons_random_graph(k, c, False))):
            num_of_connected_graph += 1
    portion = num_of_connected_graph / n
    return portion

# test both
# return index 0 for portion_cyclic_graph, index 1 for portion_connected_graph.
def get_portion_cycle_connected(n, k, c):
    num_of_cyclic_graph = 0
    num_of_connected_graph = 0
    for _ in range(n):
        g = cons_random_graph(k, c, False)
        if (has_cycle(g)):
            num_of_cyclic_graph += 1
        if (is_connected(g)):
            num_of_connected_graph += 1
    portion_cyclic_graph = num_of_cyclic_graph / n
    portion_connected_graph = num_of_connected_graph / n
    return (portion_cyclic_graph, portion_connected_graph)

# Get the average corresponding c of the half portion.
# portions - sequence of ratio.
# tolerance - (0.5 - tolerance, 0.5 + tolerance).
# Note: could raise division by zero if no points filtered.
def get_half_c(cs, portions, tolerance):
    try:
        c_seq = []
        for i in range(len(cs)):
            if (0.5 - tolerance < portions[i] < 0.5 + tolerance):
                c_seq.append(cs[i])
        ave_c = sum(c_seq) / len(c_seq)
        return ave_c
    except:
        print("EXCEPTION: Try increace more random times or tolerance!")
        
        
# random 100 times, 100 nodes, c edges
######################### has cycle experiment ###############################
# cs = list(range(100))
# portions_cycle = [get_portion_cycle(100, 100, c) for c in cs]
# plt.scatter(cs, portions_cycle, marker='.', label = "portion of cyclic graph")
# plt.xlabel("Number of edges(c)")
# plt.ylabel("Portion(%)")
# plt.legend(loc='upper left')
# plt.show()

# random 100 times, 100 nodes, c edges
######################### is connected experiment ############################
# cs = list(range(0,400))
# portions_connected = [get_portion_connected(100, 100, c) for c in cs]
# plt.scatter(cs, portions_connected, marker='.', label = "portion of connected graph")
# plt.xlabel("Number of edges(c)")
# plt.ylabel("Portion(%)")
# plt.legend(loc='upper left')
# plt.show()

# random 200 times, 100 nodes, c edges
######################## cycle & connected experiment ########################
cs = list(range(0,400))
portions = [get_portion_cycle_connected(200, 100, c) for c in cs]
portions_cycle = [portion[0] for portion in portions]
portions_connected = [portion[1] for portion in portions]
plt.scatter(cs, portions_cycle, marker='.', label = "cyclic graph")
plt.scatter(cs, portions_connected, marker='.', label = "connected graph")
plt.xlabel("Number of edges(c)")
plt.ylabel("Portion(%)")
plt.legend(loc='lower right')
plt.show()
print("the value of c which roughly half the graphs to contain a cycle: ")
print(get_half_c(cs, portions_cycle, 0.05))
print("the value of c which roughly half the graphs to be connected: ")
print(get_half_c(cs, portions_connected, 0.05))
