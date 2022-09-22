import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for verse-group ''' 
# Defining Elements
verse_group = Element('verse-group')
G_verse_group = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
# Creating the Nodes
verse_group_node = Node(element=verse_group, graph=G_verse_group)

G_verse_group.add_nodes_from([first_node, last_node, label_node, title_node, subtitle_node, verse_line_node, verse_group_node, attrib_node, permissions_node])

for i in list(G_verse_group.nodes):
    for j in list(G_verse_group.nodes):
        if i.element.name == 'first':
            if j.element.name in ['label', 'title', 'subtitle', 'verse-line', 'verse-group']:
                G_verse_group.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name in ['title', 'subtitle', 'verse-line', 'verse-group']:
                G_verse_group.add_edge(i, j)
        if i.element.name == 'subtitle':
            if j.element.name in ['verse-line', 'verse-group']:
                G_verse_group.add_edge(i, j)
        if i.element.name in ['verse-line', 'verse-group']:
            if j.element.name not in ['first', 'label', 'title', 'subtitle']:
                G_verse_group.add_edge(i, j)
        if i.element.name in ['attrib', 'permissions']:
            if j.element.name in ['attrib', 'permissions', 'last']:
                G_verse_group.add_edge(i, j)