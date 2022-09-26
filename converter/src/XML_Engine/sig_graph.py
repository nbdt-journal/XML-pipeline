import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Signature ''' 
# Defining Elements
sig = Element('sig')
G_sig = nx.DiGraph()
G_sig.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, sub_node, sup_node, named_content_node, styled_content_node, break_node, inline_graphic_node, inline_media_node, private_char_node, graphic_node, media_node])

for i in list(G_sig.nodes):
    for j in list(G_sig.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_sig.add_edge(i, j)
# Creating the Nodes
sig_node = Node(element=sig, graph=G_sig)
