#  @details All search methods in this module assume that node1 and node2 are different

from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

####################### before are original code #############################


#Turns the predecessor dictionary into a list of history
def history(pred_dict, node1, node2):
    if not bool(pred_dict):
        return []
    L = []
    current_node = node2
    while current_node != node1:
        L.append(current_node)
        current_node = pred_dict[current_node]
    return L[::-1] # reverse the list

#Breadth First Search
#return path between node1 and node2
def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    ########## comment out below to see the visiting node ############
    # print("Visiting: " + str(node1))
    pred = {}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return [node1] + history(pred, node1, current_node) + [node2]
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                ########## comment out below to see the visiting node ########
                # print("Visiting: " + str(node))
                pred[node] = current_node
    return []


#Depth First Search
#Return path between node1 and node2
def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    pred = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            ########## comment out below to see the visiting node ############
            # print("Visiting: " + str(current_node))
            for node in G.adj[current_node]:
                if node == node2:
                    return [node1] + history(pred, node1, current_node) + [node2]
                if not marked[node]:
                    S.append(node)
                    pred[node] = current_node
    return []


#Breadth First Search from node1
#return predecessor dictionary
def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1 : True}
    ########## comment out below to see the visiting node ############
    # print("Visiting: " + str(node1))
    pred = {}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                ########## comment out below to see the visiting node ########
                # print("Visiting: " + str(node))
                pred[node] = current_node
    return pred

#Depth First Search
#return predecessor dictionary
def DFS3(G, node1):
    S = [node1]
    marked = {}
    pred = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            ########## comment out below to see the visiting node ############
            # print("Visiting: " + str(current_node))
            for node in G.adj[current_node]:
                if not marked[node]:
                    S.append(node)
                    pred[node] = current_node
    return pred


def has_cycle(G):
    # for each node in the graph
    for node in G.adj:
        if has_cycle_node(G, node):
            return True
    return False
        
        
# Detect if the graph has a circle starting from a node.
# Use DFA go through the graph.
# Reuse DFA2
def has_cycle_node(G, node1):
    S = [node1]
    marked = {}
    pred = {}
    for node in G.adj:
        pred[node] = False
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            ########## comment out below to see the visiting node ############
            # print("Visiting: " + str(current_node))
            for node in G.adj[current_node]:
                if not marked[node]:
                    S.append(node)
                    pred[node] = current_node
                # if this adjacent vertice has been marked and its parent not
                # the current one, then detect a circle
                elif node != pred[current_node]:
                    return True
    return False

# Strategy: simply tranverse the graph using DFA, is all nodes are visited, 
# return True; otherwise, return False.
# Reuse DFA2
# Note: Assume graph no empty!
def is_connected(G):
    S = [0]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            ########## comment out below to see the visiting node ############
            # print("Visiting: " + str(current_node))
            for node in G.adj[current_node]:
                if not marked[node]:
                    S.append(node)
    for node in G.adj:
        if marked[node] == False:
            return False
    return True

###################################### test ##################################
# tree graph test
# G1 = Graph(12)
# G1.add_edge(8, 7)
# G1.add_edge(7, 0)
# G1.add_edge(7, 3)
# G1.add_edge(3, 6)
# G1.add_edge(3, 5)
# G1.add_edge(3, 4)
# G1.add_edge(1, 2)
# G1.add_edge(8, 1)
# G1.add_edge(1, 11)
# G1.add_edge(11, 9)
# G1.add_edge(11, 10)
# print(BFS2(G1, 8, 6))
# print(DFS2(G1, 8, 6))
# print(BFS3(G1, 8))
# print(DFS3(G1, 8))
# print(has_cycle(G1))
# print(is_connected(G1))

# the one on pdf test
# G2 = Graph(7)
# G2.add_edge(1, 2)
# G2.add_edge(2, 4)
# G2.add_edge(4, 6)
# G2.add_edge(1, 3)
# G2.add_edge(3, 4)
# G2.add_edge(4, 5)
# G2.add_edge(3, 5)
# print(BFS2(G2, 2, 3))
# print(DFS2(G2, 1, 6))
# print(BFS3(G2, 1))
# print(DFS3(G2, 1))
# print(has_cycle(G2))
# print(is_connected(G2))












