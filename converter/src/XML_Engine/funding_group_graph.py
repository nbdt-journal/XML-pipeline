import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for funding-group ''' 
# Defining Elements
funding_group = Element('funding-group')


first_node = node.get_first_node()
last_node = node.get_last_node()
G_funding_group = nx.DiGraph()

G_funding_group.add_nodes_from([first_node, last_node, award_group_node, funding_statement_node, open_access_node])

for i in list(G_funding_group.nodes):
    for j in list(G_funding_group.nodes):
        if i.element.name == 'first':
            if j.element.name != 'first':
                G_funding_group.add_edge(i, j)
        if i.element.name == 'award-group':
            if j.element.name != 'first':
                G_funding_group.add_edge(i, j)
        if i.element.name == 'funding-statement':
            if j.element.name not in ['first', 'award-group']:
                G_funding_group.add_edge(i, j)
        if i.element.name == 'open-access':
            if j.element.name in ['open-access', 'last']:
                G_funding_group.add_edge(i, j)

# Creating the Nodes
funding_group_node = Node(element=funding_group, graph=G_funding_group)