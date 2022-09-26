import networkx as nx 
from copy import deepcopy

import node
from node import Node 
from element import Element 

''' Building a graph for award-id ''' 
# Defining Elements
award_id = Element('award-id')
G_award_id = nx.DiGraph()
award_id_node = Node(element=award_id, graph=G_award_id)

G_award_id.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, sub_node, sup_node])

for i in list(G_award_id_group.nodes):
    for j in list(G_award_id_group.nodes):
       if i.element.name != 'last' and j.element.name != 'first':
        G_award_id_group.add_edge(i, j)