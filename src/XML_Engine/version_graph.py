import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for version ''' 
# Defining Elements
version = Element('version')
G_version = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_version.add_nodes_from([first_node, last_node, sub_node, sup_node])
for i in list(G_version.nodes):
    for j in list(G_version.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_version.add_edge(i, j)
# Creating the Nodes
version_node = Node(element=version, graph=G_version)