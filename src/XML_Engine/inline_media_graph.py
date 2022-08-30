import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for inline-media ''' 
# Defining Elements
inline_media = Element('inline-media')
G_inline_media = nx.DiGraph()
G_inline_media.add_nodes_from([node.get_first_node(), node.get_last_node(), alt_text_node, long_desc_node, email_node, ext_link_node, uri_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, named_content_node, styled_content_node, sub_node, sup_node])

for i in list(G_inline_media.nodes):
    for j in list(G_inline_media.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        G_inline_media.add_edge(i, j)

inline_media_node = Node(element=inline_media, graph=G_inline_media)