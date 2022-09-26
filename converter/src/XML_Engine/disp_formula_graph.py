import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for disp-formula ''' 
# Defining Elements
disp_formula = Element('disp-formula')
# Creating the Nodes
G_disp_formula = nx.DiGraph()
G_disp_formula.add_nodes_from([node.get_first_node(), node.get_last_node(), alt_text_node, long_desc_node, abstract_node, email_node, ext_link_node, uri_node, break_node, caption_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, object_id_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, kwd_group_node, subj_group_node, label_node, named_content_node, styled_content_node, tex_math_node, mml_math_node, alternatives_node, array_node, code_node, graphic_node, media_node, preformat_node, sub_node, sup_node])

disp_formula_node = Node(element=disp_formula, graph=G_disp_formula)

for i in list(G_disp_formula.nodes):
    for j in list(G_disp_formula.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_disp_formula.add_edge(i, j)

