import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for license-p ''' 
# Defining Elements
license_p = Element('license-p')
G_license_p = nx.DiGraph()
G_license_p.add_nodes_from([node.get_first_node(), node.get_last_node(), email_node, ext_link_node, uri_node, inline_supplementary_material_node, related_article_node, related_object_node, address_node, alternatives_node, answer_node, answer_set_node, array_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, explanation_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, question_node, question_wrap_node, question_wrap_group_node, supplementary_material_node, table_wrap_node, table_wrap_group_node, disp_formula_node, citation_alternatives_node, element_citation_node, mixed_citation_node, nlm_citation_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, award_id_node, funding_source_node, open_access_node, chem_struct_node, inline_formula_node, inline_graphic_node, inline_media_node, private_char_node, def_list_node, list_node, tex_math_node, mml_math_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, disp_quote_node, speech_node, statement_node, verse_group_node, fn_node, target_node, xref_node, sub_node, sup_node, price_node])

for i in list(G_license_p.nodes):
    for j in list(G_license_p.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_license_p.add_edge(i, j)

# Creating the Nodes
license_p_node = Node(element=license_p, graph=G_license_p)