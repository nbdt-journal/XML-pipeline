import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for institution ''' 
# Defining Elements 
institution = Element('institution')

G_institution = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_institution.add_nodes_from([first_node, last_node, sub_node, sup_node])
G_institution.add_edge(first_node, sub_node)
G_institution.add_edge(first_node, sup_node)
G_institution.add_edge(first_node, last_node)
G_institution.add_edge(sub_node, sub_node)
G_institution.add_edge(sub_node, sup_node)
G_institution.add_edge(sub_node, last_node)
G_institution.add_edge(sup_node, sub_node)
G_institution.add_edge(sup_node, sup_node)
G_institution.add_edge(sup_node, last_node)

# Creating the Nodes
institution_node = Node(element=institution, graph=node.get_leaf_graph())