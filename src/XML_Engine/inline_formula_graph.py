import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for inline-formula ''' 
# Defining Elements
inline_formula = Element('inline-formula')
inline_formula = nx.DiGraph()
inline_formula.add_nodes_from([node.get_first_node(), node.get_last_node(), alt_text_node, long_desc_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, alternatives_node, inline_graphic_node, inline_media_node, private_char_node, chem_struct_node, inline_formula_node, tex_math_node, mml_math_node, named_content_node, styled_content_node, sub_node, sup_node])
for i in list(inline_formula.nodes):
    for j in list(inline_formula.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        inline_formula.add_edge(i, j)

inline_formula_node = Node(element=inline_formula, graph=inline_formula)