import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Author Notes ''' 
# Defining Elements
author_notes = Element('author-notes')
# Creating the Nodes
G_author_notes = nx.DiGraph()
author_notes_node = Node(element=author_notes, graph=G_author_notes)

group_1 = [corresp_node, fn_node, p_node]
G_author_notes.add_nodes_from([label_node, title_node, node.get_first_node(), node.get_last_node()])

for i in list(G_author_notes.nodes):
    for j in list(G_author_notes.nodes):
        if i.element.name == 'first':
            if j.element.name not in ['first', 'last']:
                G_author_notes.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name not in ['first', 'label', 'last']:
                G_author_notes.add_edge(i, j)
        if i.element.name == 'title':
            if j.element.name not in ['first', 'label', 'last', 'title']:
                G_author_notes.add_edge(i, j)
        if i.element in group_1:
            if j.element in group_1 or j.element.name == 'last':
                G_author_notes.add_edge(i, j)