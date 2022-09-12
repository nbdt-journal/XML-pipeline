import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for collab ''' 
# Defining Elements
collab = Element('collab')
# Creating the Nodes
G_collab = nx.DiGraph()
G_collab.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, sub_node, sup_node, addr_line_node, city_node, country_node, fax_node, institution_node, institution_wrap_node, phone_node, postal_code_node, state_node, contrib_group_node, address_node, aff_node, aff_alternatives_node, author_comment_node, bio_node, email_node, ext_link_node, on_behalf_of_node, role_node, uri_node, xref_node, fn_node])

collab_node = Node(element=collab, graph=G_collab)

for i in list(G_collab.nodes):
    for j in list(G_collab.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_collab.add_edge(i, j)

