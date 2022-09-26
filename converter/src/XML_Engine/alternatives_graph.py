import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for alternatives ''' 
# Defining Elements
alternatives = Element('alternatives')
G_alternatives = nx.DiGraph()
# Creating the Nodes
alternatives_node = Node(element=alternatives, graph=G_alternatives)
first_node = node.get_first_node()
last_node = node.get_last_node()
G_alternatives.add_nodes_from([first_node, last_node, object_id, array_node, chem_struct_node, code_node, graphic_node, inline_graphic_node, inline_media_node, inline_supplementary_material_node, media_node, preformat_node, private_char_node, supplementary_material_node, table_node, textual_form_node, tex_math_node, mml_math_node])
for i in list(G_alternatives.nodes):
    for j in list(G_alternatives.nodes):
        if i.element.name == 'last':
            break
        if i.element.name == 'first' and j.element.name == 'last':
            continue
        if i.element.name == 'object-id':
            if j.element.name == 'last':
                continue
        else:
            if i.element.name != 'first' and j.element.name == 'object-id':
                continue 
        if j.element.name == 'first':
            continue 
        if j.element.anme == 'object-id' and i.element.name != 'object-id':
            continue
        G_alternatives.add_edge(i, j)
