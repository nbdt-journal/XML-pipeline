import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Back ''' 
# Defining Elements
back = Element('back')
# Creating the Nodes
G_back = nx.DiGraph()
group_1 = [ack_node, app_group_node, bio_node, fn_group_node, glossary_node, ref_list_node, notes_node, sec_node]
G_back.add_nodes_from([label_node, title_node, node.get_first_node(), node.get_last_node()])
G_back.add_nodes_from(group_1)

back_node = Node(element=back, graph=G_back)

for i in list(G.nodes):
    for j in list(G.nodes):
        if i.element.name == 'first':
            if j.element.name != 'first':
                G_back.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name not in ['first', 'label']:
                G_back.add_edge(i, j)
        if i.element.name == 'title':
            if j.element.name not in ['first', 'label']:
                G_back.add_edge(i, j)
        if i.element in group_1:
            if j.element in group_1 or j.element.name == 'last':
                G_back.add_edge(i, j)