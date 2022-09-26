import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Speaker ''' 
# Defining Elements
speaker = Element('speaker')
G_speaker = nx.DiGraph()
G_speaker.add_nodes_from([node.get_first_node(), node.get_last_node(), degrees_node, given_names_node, prefix_node, surname_node, suffix_node, fn_node, target_node, xref_node])

for i in list(G_speaker.nodes):
    for j in list(G_speaker.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_speaker.add_edge(i, j)
# Creating the Nodes
speaker_node = Node(element=speaker, graph=G_speaker)
