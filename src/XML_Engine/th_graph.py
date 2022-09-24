import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Table Header Cell''' 
# Defining Elements
th = Element('th')
G_th = nx.DiGraph()
G_th.add_nodes_from([node.get_first_node(), node.get_last_node(), email_node, ext_link_node, uri_node, hr_node, inline_supplementary_material_node, related_article_node, related_object_node, disp_formula_node, disp_formula_group_node, break_node, citation_alternatives_node, element_citation_node, mixed_citation_node, nlm_citation_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, disp_quote_node, speech_node, statement_node, verse_group_node, def_list_node, list_node, tex_math_node, mml_math_node, p_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, alternatives_node, array_node, code_node, graphic_node, media_node, preformat_node, answer_node, answer_set_node, explanation_node, question_node, question_wrap_node, question_wrap_group_node, fn_node, target_node, xref_node, sub_node, sup_node])

for i in list(G_th.nodes):
    for j in list(G_th.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_th.add_edge(i, j)
# Creating the Nodes
th_node = Node(element=th, graph=G_th)
