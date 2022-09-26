import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for textual-form ''' 
# Defining Elements
textual_form = Element('textual-form')
G_textual_form = nx.DiGraph()
G_textual_form.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, inline_graphic_node, inline_media_node, private_char_node, tex_math_node, mml_math_node, named_content_node, styled_content_node, sub_node, sup_node])

for i in list(G_textual_form.nodes):
    for j in list(G_textual_form.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_textual_form.add_edge(i, j)
# Creating the Nodes
textual_form_node = Node(element=textual_form, graph=G_textual_form)
