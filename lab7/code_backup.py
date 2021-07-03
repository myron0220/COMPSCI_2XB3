from graphs import *

import matplotlib.pyplot as plt
import random

# def test_graph():
#     n = 6
#     g = Graph(n + 1)
#     g.add_edge(1, 2)
#     g.add_edge(1, 3)
#     g.add_edge(2, 4)
#     g.add_edge(3, 4)
#     g.add_edge(3, 5)
#     g.add_edge(4, 5)
#     g.add_edge(4, 6)
#     print(g.number_of_nodes())
#     for i in range(n + 1):
#         print(i, g.adjacent_nodes(i))
#     print(g.are_connected(1, 6))
#     print(g.are_connected(1, 2))
#     print(BFS(g, 1, 6))
#     print(DFS(g, 1, 6))
#     print(BFS2(g, 1, 6))
#     print(DFS2(g, 1, 6))
#     print(BFS3(g, 1))
#     print("H", DFS3(g, 1))
#     print(has_cycle(g))
#     print(is_connected(g))


# def test_cycle_connected():
#     n = 6
#     g = Graph(n + 1)
#     g.add_edge(1, 2)
#     g.add_edge(1, 3)
#     g.add_edge(2, 4)
#     g.add_edge(3, 5)
#     g.add_edge(4, 6)
#     print(g.number_of_nodes())
#     for i in range(n + 1):
#         print(i, g.adjacent_nodes(i))
#     print(has_cycle(g) == False)
#     print(is_connected(g) == False)
#     g.add_edge(0, 2)
#     print(is_connected(g) == True)
#     g.add_edge(3, 2)
#     print(has_cycle(g) == True)

# def test_dfs2():
#     G = Graph(12)
#     G.add_edge(8, 7)
#     G.add_edge(7, 0)
#     G.add_edge(7, 3)
#     G.add_edge(3, 6)
#     G.add_edge(3, 5)
#     G.add_edge(3, 4)
#     G.add_edge(1, 2)
#     G.add_edge(8, 1)
#     G.add_edge(1, 11)
#     G.add_edge(11, 9)
#     G.add_edge(11, 10)
#     print(DFS(G, 8, 6))
#     print()
#     print(DFS2(G, 8, 6))



# test_graph()
#test_cycle_connected()
#test_dfs2()
    
##################### cycles test ######################
nodes = 100
number_of_graphs = 100
edges = [i for i in range(1, 401, 1)]
cycle_portions = []

for edge in edges:
    num_has_cycle = 0 
    for _ in range(number_of_graphs):
        g = Graph(nodes)
        node_pairs = []
        # make different edge pairs
        while len(node_pairs) != edge:
            a = random.randint(0,99)
            b = random.randint(0,99)
            if (a,b) not in node_pairs and (b, a) not in node_pairs and a != b:
                node_pairs.append((a,b))
        # make edges
        for node_pair in node_pairs:
            g.add_edge(node_pair[0], node_pair[1])
        # the number of graphs has a cycle
        if has_cycle(g):
            num_has_cycle += 1
    cycle_portions.append(num_has_cycle/number_of_graphs)

print("Portion(cycle): ", num_has_cycle/number_of_graphs)


##################### connected test ######################
nodes = 100
number_of_graphs = 100
connect_portions = []

for edge in edges:
    num_has_connection = 0 
    for _ in range(number_of_graphs):
        g = Graph(nodes)
        node_pairs = []
        # make different edge pairs
        while len(node_pairs) != edge:
            a = random.randint(0,99)
            b = random.randint(0,99)
            if (a,b) not in node_pairs and (b, a) not in node_pairs and a != b:
                node_pairs.append((a,b))
        # make edges
        for node_pair in node_pairs:
            g.add_edge(node_pair[0], node_pair[1])
        # the number of graphs has a cycle
        if is_connected(g):
            num_has_connection += 1
    connect_portions.append(num_has_connection/number_of_graphs)
    
print("Portion(connected): ", num_has_connection/number_of_graphs)

plt.scatter(edges, cycle_portions, label = "cyclic graph")
plt.scatter(edges, connect_portions, label = "connected graph")
plt.xlabel("Number of edges(c)")
plt.ylabel("Portion")
plt.legend(loc='lower right')
plt.savefig("Figures/" + "Graph_test")
plt.show()
plt.close()