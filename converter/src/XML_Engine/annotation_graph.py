import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for annotation ''' 
# Defining Elements
annotation = Element('annotation')
G_annotation = nx.DiGraph()
G_annotation.add_nodes_from([node.get_first_node(), node.get_last_node(), p_node])
annotation_node = Node(element=annotation, graph=G_annotation)

G_annotation.add_edge(first_node, p)
G_annotation.add_edge(p, p)
G_annotation.add_edge(p, last_node)