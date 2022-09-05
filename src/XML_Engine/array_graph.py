import networkx as nx 
from copy import deepcopy

import node
from node import Node 
from element import Element 

''' Building a graph for template ''' 
# Defining Elements
template = Element('template')
G_template = nx.DiGraph()
template_node = Node(element=template, graph=G_template)

group_1 = [alt_text_node, long_desc_node, email_node, ext_link_node, uri_node]
group_2 = [alternatives_node, graphic_node, media_node]
group_3 = [tbody_node]
group_4 = [attrib_node, permissions_node]
G_template.add_nodes_from(group_1)
G_template.add_nodes_from(group_2)
G_template.add_nodes_from(group_3)
G_template.add_nodes_from(group_4)
G_template.add_nodes_from([node.get_first_node(), node.get_last_node()])

for i in list(G_template_group.nodes):
    for j in list(G_template_group.nodes):
        if i.element.name == 'first':
            if j.element in group_1 or j.element in group_2 or j.element in group_3:
                G_template.add_edge(i, j)
        if i.element.name in group_1:
            if j.element in group_1 or j.element in group_2 or j.element in group_3:
                G_template.add_edge(i, j)
        if i.element in group_2:
            if j.element not in group_1 and j.element not in group_3 or j.element.name == 'last':
                G_template.add_edge(i, j)
        if i.element in group_3:
            if j.element in group_4 or j.element.name == 'last':
                G_template.add_edge(i, j)
        if i.element in group_4:
            if j.element in group_4 or j.element.name == 'last':
                G_template.add_edge(i, j)