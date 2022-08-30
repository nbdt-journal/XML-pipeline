import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for italic ''' 
# Defining Elements
italic = Element('italic')
G_italic = nx.DiGraph()
# Creating the Nodes
italic_node = Node(element=italic, graph=G_italic)
G_italic.add_nodes_from([node.get_first_node(), node.get_last_node(), email_node, ext_link_node, uri_node, inline_supplementary_material_node])
for i in list(G_italic.nodes):
    for j in list(G_italic.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        G_italic.add_edge(i, j)