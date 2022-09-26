import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for chapter_title ''' 
# Defining Elements
chapter_title = Element('chapter-title')
# Creating the Nodes
G_chapter_title = nx.DiGraph()
chapter_title_node = Node(element=chapter_title, graph=G_chapter_title)

for i in list(G_chapter_title.nodes):
    for j in list(G_chapter_title.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_chapter_title.add_edge(i, j)