import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for inline-supplementary-material ''' 
# Defining Elements
inline_supplementary_material = Element('inline-supplementary-material')
G_inline_supplementary_material = nx.DiGraph()
G_inline_supplementary_material.add_nodes_from([node.get_first_node(), node.get_last_node(), alternatives_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, supplementary_material_node, table_wrap_node, table_wrap_group_node])

for i in list(G_inline_supplementary_material.nodes):
    for j in list(G_inline_supplementary_material.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_inline_supplementary_material.add_edge(i, j)

# Creating the Nodes
inline_supplementary_material_node = Node(element=inline_supplementary_material, graph=G_inline_supplementary_material)
