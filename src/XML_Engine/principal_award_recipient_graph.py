import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for principal-award-recipient ''' 
# Defining Elements
principal_award_recipient = Element('principal-award-recipient')
G_principal_award_recipient = nx.DiGraph()
G_principal_award_recipient.add_nodes_from([node.get_first_node(), node.get_last_node(), contrib_id_node, name_node, name_alternatives_node, institution_node, institution_wrap_node, string_name_node])

for i in list(G_principal_award_recipient.nodes):
    for j in list(G_principal_award_recipient.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_principal_award_recipient.add_edge(i, j)
# Creating the Nodes
principal_award_recipient_node = Node(element=principal_award_recipient, graph=G_principal_award_recipient)
