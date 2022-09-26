import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for principal-investigator ''' 
# Defining Elements
principal_investigator = Element('principal-investigator')
G_principal_investigator = nx.DiGraph()
G_principal_investigator.add_nodes_from([node.get_first_node(), node.get_last_node(), contrib_id_node, name_node, name_alternatives_node, string_name_node])

for i in list(G_principal_investigator.nodes):
    for j in list(G_principal_investigator.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_principal_investigator.add_edge(i, j)
# Creating the Nodes
principal_investigator_node = Node(element=principal_investigator, graph=G_principal_investigator)
