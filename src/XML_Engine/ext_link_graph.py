import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for ext-link ''' 
# Defining Elements
ext_link = Element('ext-link')
G_ext_link = nx.DiGraph()
# Creating the Nodes
ext_link_node = Node(element=ext_link, graph=node.get_leaf_graph())
G_ext_link.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, unerline_node, ruby_node, named_content_node, styled_content_node, sub_node, sup_node])

for i in list(G_ext_link.nodes):
    for j in list(G_ext_link.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        G_ext_link.add_edge(i, j)