import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Standards Organization ''' 
# Defining Elements
std_organization = Element('std_organization')
G_std_organization = nx.DiGraph()
G_std_organization.add_nodes_from([node.get_first_node(), node.get_last_node(), institution_node, institution_wrap_node, sub_node, sup_node])

for i in list(G_std_organization.nodes):
    for j in list(G_std_organization.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_std_organization.add_edge(i, j)
# Creating the Nodes
std_organization_node = Node(element=std_organization, graph=G_std_organization)
