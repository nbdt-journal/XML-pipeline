import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for resource-name ''' 
# Defining Elements
resource_name = Element('resource-name')
G_resource_name = nx.DiGraph()
G_resource_name.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, sub_node, sup_node])

for i in list(G_resource_name.nodes):
    for j in list(G_resource_name.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_resource_name.add_edge(i, j)
# Creating the Nodes
resource_name_node = Node(element=resource_name, graph=G_resource_name)
