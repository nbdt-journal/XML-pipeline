import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for copyright-holder ''' 
# Defining Elements
copyright_holder = Element('copyright-holder')
# Creating the Nodes
G_copyright_holder = nx.DiGraph()
G_copyright_holder.add_nodes_from([node.get_first_node(), node.get_last_node(), institution_node, institution_wrap_node, sub_node, sup_node])
copyright_holder_node = Node(element=copyright_holder, graph=G_copyright_holder)

for i in list(G_copyright_holder.nodes):
    for j in list(G_copyright_holder.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_copyright_holder.add_edge(i, j)

