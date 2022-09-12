import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for compound-kwd-part ''' 
# Defining Elements
compound_kwd_part = Element('compound-kwd-part')
# Creating the Nodes
G_compound_kwd_part = nx.DiGraph()
G_compound_kwd_part.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, named_content_node, styled_content_node, fn_node, target_node, xref_node, sub_node, sup_node])

compound_kwd_part_node = Node(element=compound_kwd_part, graph=G_compound_kwd_part)

for i in list(G_compound_kwd_part.nodes):
    for j in list(G_compound_kwd_part.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_compound_kwd_part.add_edge(i, j)

