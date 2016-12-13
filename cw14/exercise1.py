#!/usr/bin/python

# Exercise 14.1
def list_nodes(graph):
    return [node for node in graph]

def list_edges(graph):
    edges = []
    for start_node, end_nodes in graph.items():
        edges += (start_node, end_node) for end_node in end_nodes
    return edges
    

def count_nodes(graph):
    return len(graph)

def count_edges(graph):
    return sum(len(end_nodes) for start_node, end_nodes in graph.items())     

# Exercise 14.3
def save_edges(graph, filename):
    edges = []
    f = open(filename) 
    for start_node, end_nodes in graph.items():
        f.write(str(start_node, end_node)+"\n" for end_node in end_nodes)

# Exercise 14.6
def node_degree(graph):
    return {start_node: len(end_nodes) 
            for start_node, end_nodes in graph.items()}
