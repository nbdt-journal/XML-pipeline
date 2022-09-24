import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for target ''' 
# Defining Elements
target = Element('target')
G_target = nx.DiGraph()
G_target.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, named_content_node, styled_content_node, sub_node, sup_node])

for i in list(G_target.nodes):
    for j in list(G_target.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_target.add_edge(i, j)
# Creating the Nodes
target_node = Node(element=target, graph=G_target)
