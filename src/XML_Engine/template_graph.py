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


for i in list(G_template_group.nodes):
    for j in list(G_template_group.nodes):
       if i.element.name != 'last' and j.element.name != 'first':
        G_template_group.add_edge(i, j)