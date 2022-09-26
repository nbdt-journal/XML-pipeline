import networkx as nx 
from copy import deepcopy

import node
from node import Node 
from element import Element 

''' Building a graph for attrib ''' 
# Defining Elements
attrib = Element('attrib')
G_attrib = nx.DiGraph()
attrib_node = Node(element=attrib, graph=G_attrib)

G_attrib.add_nodes_from([node.get_first_node(), node.get_last_node(), email_node, ext_link_node, uri_node, inline_supplementary_material_node, related_article_node, related_object_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, tex_math_node, mml_math_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, fn_node, target_node, xref_node, sub_node, sup_node, break_node])

for i in list(G_attrib_group.nodes):
    for j in list(G_attrib_group.nodes):
        if j.element.name == 'first' or i.element.name == 'last':
            continue
        else:
            G_attrib.add_edge(i, j)