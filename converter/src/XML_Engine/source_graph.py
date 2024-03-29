import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Source ''' 
# Defining Elements
source = Element('source')
G_source = nx.DiGraph()
G_source.add_nodes_from([node.get_first_node(), node.get_last_node(), abbrev_node, email_node, ext_link_node, uri_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, tex_math_node, mml_math_node, named_content_node, styled_content_node, fn_node, target_node, xref_node, sub_node, sup_node])

for i in list(G_source.nodes):
    for j in list(G_source.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_source.add_edge(i, j)
# Creating the Nodes
source_node = Node(element=source, graph=G_source)
