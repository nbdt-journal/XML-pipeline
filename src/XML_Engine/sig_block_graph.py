import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for sig-block ''' 
# Defining Elements
sig_block = Element('sig-block')
G_sig_block = nx.DiGraph()
G_sig_block.add_nodes_from([node.get_first_node(), node.get_last_node(), break_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, graphic_node, media_node, inline_graphic_node, inline_media_node, private_char_node, named_content_node, styled_content_node, sig_node, sub_node, sup_node])

for i in list(G_sig_block.nodes):
    for j in list(G_sig_block.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_sig_block.add_edge(i, j)
# Creating the Nodes
sig_block_node = Node(element=sig_block, graph=G_sig_block)
