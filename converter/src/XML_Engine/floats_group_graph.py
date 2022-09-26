import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for floats-group ''' 
# Defining Elements
floats_group = Element('floats-group')
G_floats_group = nx.DiGraph()
G_floats_group.add_nodes_from([node.get_first_node(), node.get_last_node(), alternatives_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, supplementary_material_node, table_wrap_node, table_wrap_group_node])

for i in list(G_floats_group.nodes):
    for j in list(G_floats_group.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_floats_group.add_edge(i, j)

# Creating the Nodes
floats_group_node = Node(element=floats_group, graph=G_floats_group)
