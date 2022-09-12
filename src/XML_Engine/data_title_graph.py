import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for data-title ''' 
# Defining Elements
data_title = Element('data-title')
# Creating the Nodes
G_data_title = nx.DiGraph()
G_data_title.add_nodes_from([node.get_first_node(), node.get_last_node(), email_node, ext_link_node, uri_node, inline_graphic_node, inline_media_node, private_char_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, named_content_node, styled_content_node, sub_node, sup_node])




data_title_node = Node(element=data_title, graph=G_data_title)

for i in list(G_data_title.nodes):
    for j in list(G_data_title.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_data_title.add_edge(i, j)

