import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for def-list ''' 
# Defining Elements
def_list = Element('def-list')
G_def_list = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_def_list.add_nodes_from([first_node, last_node, label_node, title_node, term_head_node, def_head_node, def_item_node, def_list_node])
for i in list(G_def_list.nodes):
    for j in list(G_def_list.nodes):
        if i.element.name == 'first':
            if j.element.name != 'first':
                G_def_list.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name not in ['first', 'label']:
                G_def_list.add_edge(i, j)
        if i.element.name == 'term-head':
            if j.element.name not in ['first', 'label', 'term-head']:
                G_def_list.add_edge(i, j)
        if i.element.name == 'def-head':
            if j.element.name not in ['first', 'label', 'term-head', 'def-head']:
                G_def_list.add_edge(i, j)
        if i.element.name == 'def-item':
            if j.element.name not in ['first', 'label', 'term-head', 'def-head']:
                G_def_list.add_edge(i, j)
        if i.element.name == 'def-list':
            if j.element.name not in ['first', 'label', 'term-head', 'def-head', 'def-item']:
                G_def_list.add_edge(i, j)
# Creating the Nodes
def_list_node = Node(element=def_list, graph=G_def_list)