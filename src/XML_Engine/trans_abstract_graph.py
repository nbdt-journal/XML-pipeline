import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for trans-abstract ''' 
# Defining Elements
trans_abstract = Element('trans-abstract')
G_trans_abstract = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_trans_abstract.add_nodes_from([first_node, last_node, object_id_node, label_node, title_node, p_node, sec_node])
for i in list(G_trans_abstract.nodes):
    for j in list(G_trans_abstract.nodes):
        if i.element.name == 'first' or i.element.name == 'object-id':
            if j.element.name != 'first':
                G_trans_abstract.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name not in ['first', 'object-id', 'label']:
                G_trans_abstract.add_edge(i, j)
        if i.element.name == 'title':
            if j.element.name not in ['first', 'object-id', 'label', 'title']:
                G_trans_abstract.add_edge(i, j)
        if i.element.name == 'p':
            if j.element.name not in ['first', 'object-id', 'label', 'title']:
                G_trans_abstract.add_edge(i, j)
        if i.element.name == 'sec':
            if j.element.name not in ['first', 'object-id', 'label', 'title', 'p']:
                G_trans_abstract.add_edge(i, j)

# Creating the Nodes
trans_abstract_node = Node(element=trans_abstract, graph=G_trans_abstract)