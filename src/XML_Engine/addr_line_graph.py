import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for addr-line ''' 
# Defining Elements
addr_line = Element('addr-line')
G_addr_line = nx.DiGraph()
G_addr_line.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, abbrev_node, index_term_node, index_term_range_end_node, milestone_end_node, milestone_start_node, named_content_node, styled_content_node, sub_node, sup_node, city_node, country_node, fax_node, institution_node, institution_wrap_node, phone_node, postal_code_node, state_node])
for i in list(G_addr_line.nodes):
    for j in list(G_addr_line.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        G_addr_line.add_edge(i, j)

addr_line_node = Node(element=addr_line, graph=G_addr_line)