import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for conf-theme ''' 
# Defining Elements
conf_theme = Element('conf-theme')
# Creating the Nodes
G_conf_theme = nx.DiGraph()
G_conf_theme.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, sub_node, sup_node])

conf_theme_node = Node(element=conf_theme, graph=G_conf_theme)

for i in list(G_conf_theme.nodes):
    for j in list(G_conf_theme.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_conf_theme.add_edge(i, j)

