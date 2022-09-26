import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for funding-source ''' 
# Defining Elements
funding_source = Element('funding-source')
G_funding_source = nx.DiGraph()
G_funding_source.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, sub_node, sup_node, institution_node, institution_wrap_node])

for i in list(G_funding_source.nodes):
    for j in list(G_funding_source.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_funding_source.add_edge(i, j)

# Creating the Nodes
funding_source_node = Node(element=funding_source, graph=G_funding_source)
