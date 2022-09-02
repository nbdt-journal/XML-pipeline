import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Aff ''' 
# Defining Elements
aff = Element('aff')
# Creating the Nodes
G_aff = nx.DiGraph()
aff_node = Node(element=aff, graph=G_aff)

G_aff.add_nodes_from([node.get_first_node(), node.get_last_node(), addr_line_node, city_node, country_node, fax_node, institution_node, institution_wrap_node, phone_node, postal_code_node, state_node, email_node, ext_link_node, uri_node, inline_supplementary_material_node, related_article_node, related_object_node, break_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, label_node, fn_node, target_node, xref_node, sub_node, sup_node])

for i in list(G_aff.nodes):
    for j in list(G_aff.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        G_aff.add_edge(i, j)
