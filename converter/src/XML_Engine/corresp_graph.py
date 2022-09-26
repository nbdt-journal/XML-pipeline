import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for corresp ''' 
# Defining Elements
corresp = Element('corresp')
# Creating the Nodes
G_corresp = nx.DiGraph()
G_corresp.add_nodes_from([node.get_first_node(), node.get_last_node(), addr_line_node, city_node, country_node, fax_node, institution_node, institution_wrap_node, phone_node, postal_code_node, state_node, email_node, ext_link_node, uri_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, label_node, named_content_node, styled_content_node, sub_node, sup_node])
corresp_node = Node(element=corresp, graph=G_corresp)

for i in list(G_corresp.nodes):
    for j in list(G_corresp.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_corresp.add_edge(i, j)

