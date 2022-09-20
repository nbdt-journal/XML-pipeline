import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Element Citation ''' 
# Defining Elements
element_citation = Element('element-citation')
G_element_citation = nx.DiGraph()
G_element_citation.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, label_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, annotation_node, article_title_node, chapter_title_node, collab_node, collab_alternatives_node, comment_node, conf_acronym_node, conf_date_node, conf_loc_node, conf_name_node, conf_sponsor_node, data_title_node, date_node, date_in_citation_node, day_node, edition_node, email_node, elocation_id_node, etal_node, ext_link_node, fpage_node, gov_node, institution_node, institution_wrap_node, isbn_node, issn_node, issn_l_node, issue_node, issue_id_node, issue_part_node, issue_title_node, lpage_node, month_node, name_node, name_alternatives_node, object_id_node, page_range_node, part_title_node, patent_node, person_group_node, pub_id_node, publisher_loc_node, publisher_name_node, role_node, season_node, series_node, size_node, source_node, std_node, string_date_node, string_name_node, supplement_node, trans_source_node, trans_title_node, uri_node, version_node, volume_node, volume_id_node, volume_series_node, year_node, sub_node, sup_node])

for i in list(G_element_citation.nodes):
    for j in list(G_element_citation.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_element_citation.add_edge(i, j)

# Creating the Nodes
element_citation_node = Node(element=element_citation, graph=G_element_citation)
