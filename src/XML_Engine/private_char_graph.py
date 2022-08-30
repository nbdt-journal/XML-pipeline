import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for private-char ''' 
# Defining Elements
private_char = Element('private-char')
G_private_char = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_private_char.add_nodes_from([first_node, last_node, glyph_data_node, glyph_ref_node, inline_graphic_node])
private_char_node = Node(element=private_char, graph=G_private_char)
G_private_char.add_edge(first_node, glyph_data_node)
G_private_char.add_edge(first_node, glyph_ref_node)
G_private_char.add_edge(first_node, inline_graphic_node)
G_private_char.add_edge(glyph_data_node, inline_graphic_node)
G_private_char.add_edge(glyph_ref_node, inline_graphic_node)
G_private_char.add_edge(glyph_data_node, last_node)
G_private_char.add_edge(glyph_ref_node, last_node)
G_private_char.add_edge(inline_graphic_node, inline_graphic_node)
G_private_char.add_edge(inline_graphic_node, last_node)

