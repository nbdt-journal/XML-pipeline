import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for rb ''' 
# Defining Elements
rb = Element('rb')
G_rb = nx.DiGraph()
# Creating the Nodes
rb_node = Node(element=rb, graph=G_rb)
G_rb.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node])

for i in list(G_rb.nodes):
    for j in list(G_rb.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        G_rb.add_edge(i, j)