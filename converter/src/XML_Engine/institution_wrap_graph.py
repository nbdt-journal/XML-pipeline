import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for institution-wrap ''' 
# Defining Elements
institution_wrap = Element('institution-wrap')

G_institution_wrap = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_institution_wrap.add_nodes_from([institution_node, first_node, last_node, institution_id_node])

for i in list(G_institution_wrap.nodes):
    for j in list(G_institution_wrap.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_institution_wrap.add_edge(i, j)

# Creating the Nodes
institution_wrap_node = Node(element=institution_wrap, graph=G_institution_wrap)