import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Standard, Cited ''' 
# Defining Elements
std = Element('std')
G_std = nx.DiGraph()
G_std.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, inline_graphic_node, inline_media_node, private_char_node, named_content_node, styled_content_node, day_node, month_node, pub_id_node, source_node, std_organization_node, year_node, sub_node, sup_node])

for i in list(G_std.nodes):
    for j in list(G_std.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_std.add_edge(i, j)
# Creating the Nodes
std_node = Node(element=std, graph=G_std)
