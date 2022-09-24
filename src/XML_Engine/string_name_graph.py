import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for string-name ''' 
# Defining Elements
string_name = Element('string-name')
G_string_name = nx.DiGraph()
G_string_name.add_nodes_from([node.get_first_node(), node.get_last_node(), degrees_node, given_names_node, prefix_node, surname_node, suffix_node])

for i in list(G_string_name.nodes):
    for j in list(G_string_name.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_string_name.add_edge(i, j)
# Creating the Nodes
string_name_node = Node(element=string_name, graph=G_string_name)
