import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for index-term ''' 
# Defining Elements
index_term_graph = Element('index-term')
# Creating the Nodes
G_index_term = nx.DiGraph()
index_term_graph_node = Node(element=index_term_graph, graph=G_index_term)

first_node = node.get_first_node()
last_node = node.get_last_node()
G_index_term.add_nodes_from([first_node, last_node, term_node, index_term_node, see_node, see_also_node])
G_index_term.add_edge(first_node, term_node)
G_index_term.add_edge(term_node, index_term_node)
G_index_term.add_edge(term_node, see_node)
G_index_term.add_edge(term_node, see_also_node)
G_index_term.add_edge(term_node, last_node)
G_index_term.add_edge(index_term_node, last_node)
G_index_term.add_edge(see_node, see_node)
G_index_term.add_edge(see_node, see_also_node)
G_index_term.add_edge(see_also_node, see_node)
G_index_term.add_edge(see_also_node, see_also_node)
G_index_term.add_edge(see_node, last_node)
G_index_term.add_edge(see_also_node, last_node)