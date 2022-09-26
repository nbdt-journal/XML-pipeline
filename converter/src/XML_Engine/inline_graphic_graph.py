import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for inline-graphic ''' 
# Defining Elements
inline_graphic = Element('inline-graphic')
G_inline_graphic = nx.DiGraph()
G_inline_graphic.add_nodes_from([node.get_first_node(), node.get_last_node(), alt_text_node, long_desc_node])

for i in list(G_inline_graphic.nodes):
    for j in list(G_inline_graphic.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        G_inline_graphic.add_edge(i, j)

inline_graphic_node = Node(element=inline_graphic, graph=G_inline_graphic)