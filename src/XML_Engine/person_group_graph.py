import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Person Group ''' 
# Defining Elements
person_group = Element('person-group')
G_person_group = nx.DiGraph()
G_person_group.add_nodes_from([node.get_first_node(), node.get_last_node(), anonymous_node, collab_node, collab_alternatives_node, name_node, name_alternatives_node, string_name_node, aff_node, aff_alternatives_node, etal_node, role_node])

for i in list(G_person_group.nodes):
    for j in list(G_person_group.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_person_group.add_edge(i, j)
# Creating the Nodes
person_group_node = Node(element=person_group, graph=G_person_group)
