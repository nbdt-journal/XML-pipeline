import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for chem-struct ''' 
# Defining Elements
chem_struct = Element('chem-struct')
G_chem_struct = nx.DiGraph()
G_chem_struct.add_nodes_from([node.get_first_node(), node.get_last_node(), alt_text_node, long_desc_node, email_node, ext_link_node, uri_node, break_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, label_node, def_list_node, list_node, tex_math_node, mml_math_node, named_content_node, styled_content_node, alternatives_node, array_node, code_node, graphic_node, media_node, preformat_node, fn_node, target_node, xref_node, sub_node, sup_node])

for i in list(G_chem_struct.nodes):
    for j in list(G_chem_struct.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        G_chem_struct.add_edge(i, j)

chem_struct_node = Node(element=chem_struct, graph=G_chem_struct)