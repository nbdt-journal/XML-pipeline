import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Label ''' 
# Defining Elements
label = Element('label')
G_label = nx.DiGraph()
G_label.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, sub_node, sup_node])

for i in list(G_label.nodes):
    for j in list(G_label.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_label.add_edge(i, j)
# Creating the Nodes
label_node = Node(element=label, graph=G_label)
