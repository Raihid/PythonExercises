#!/usr/bin/python
import random


# Exercise 14.1
def list_nodes(graph):
    return [node for node in graph]


def list_edges(graph):
    edges = []
    for start_node, end_nodes in graph.items():
        edges += [(start_node, end_node) for end_node in end_nodes]
    return edges


def count_nodes(graph):
    return len(graph)


def count_edges(graph):
    return sum(len(end_nodes) for start_node, end_nodes in graph.items())


print("\n----- Testing exercise 14.1 -----")
test_graph = {0: {1: 3, 2: 4}, 1: {0: 1, 2: 1}, 2: {0: 5, 1: 10}}
print("Our test graph: " + str(test_graph))
print("Nodes in test graph: " + str(list_nodes(test_graph)))
print("Edges in test graph: " + str(list_edges(test_graph)))
print("The number of nodes in test graph is " +
      str(count_nodes(test_graph)))
print("The number of edges in test graph is " +
      str(count_edges(test_graph)))


# Exercise 14.3
def save_edges(graph, filename):
    f = open(filename, "w")
    for start_node, end_nodes in graph.items():
        out_lines = "\n".join(str(start_node) + " " + str(end_node)
                              for end_node in end_nodes)
        print(out_lines)
        f.write(out_lines)
        f.write("\n")


print("\n----- Testing exercise 14.3 ------")
print("Output: ")
save_edges(test_graph, "graph.dat")


# Exercise 14.5
def make_complete(n):
    graph = {i: {} for i in range(n)}
    for i in range(n):
        graph[i] = {}
        for j in range(n-1):
            if i == j:
                continue
            graph[i][j] = random.randint(0, 99)
            graph[j][i] = graph[i][j]
    return graph


def make_cyclic(n):
    graph = {i: {} for i in range(n)}
    for i in range(n-1):
        dist = random.randint(0, 99)
        graph[i][i+1] = dist
        graph[i+1][i] = dist
    dist = random.randint(0, 99)
    graph[n-1][0] = dist
    graph[0][n-1] = dist

    return graph


def make_tree(n):
    if n == 0:
        return
    graph = {i: {} for i in range(n)}
    current = 0
    count = 1
    while n > count:
        graph[current] = graph.get(current, {})
        for k in range(1, min(2, n - count) + 1):
            graph[current][2 * current + k] = True
            graph[2 * current + k] = graph.get(2 * current + k, {})
            graph[2 * current + k][current] = True
            count += 1
        current += 1
    return graph


# Exercise 14.6
def node_degree(graph):
    return {start_node: len(end_nodes)
            for start_node, end_nodes in graph.items()}


print("\n----- Testing exercise 14.5 and 14.6 -----")
gen_tree = make_tree(5)
print("Generated tree: " + str(gen_tree))
print("Node degrees in generated tree: " +
      str(node_degree(gen_tree)))
gen_cyclic = make_cyclic(10)
print("Generated cycle graph: " + str(gen_cyclic))
print("Node degrees in generated cyclic graph: " +
      str(node_degree(gen_cyclic)))
gen_complete = make_complete(5)
print("Generated complete graph: " + str(gen_complete))
print("Node degrees in generated complete graph: " +
      str(node_degree(gen_complete)))
