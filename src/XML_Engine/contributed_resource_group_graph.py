import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for contributed-resource-group ''' 
# Defining Elements
contributed_resource_group = Element('contributed-resource-group')
# Creating the Nodes
G_contributed_resource_group = nx.DiGraph()
contributed_resource_group_node = Node(element=contributed_resource_group, graph=G_contributed_resource_group)

first_node = node.get_first_node()
last_node = node.get_last_node()
G_contributed_resource_group.add_nodes_from([first_node, last_node, award_group_node, support_description_node, resource_group_node])
G_contributed_resource_group.add_edge(first_node, award_group_node)
G_contributed_resource_group.add_edge(first_node, support_description_node)
G_contributed_resource_group.add_edge(first_node, resource_group_node)
G_contributed_resource_group.add_edge(first_node, last_node)
G_contributed_resource_group.add_edge(award_group_node, award_group_node)
G_contributed_resource_group.add_edge(award_group_node, support_description_node)
G_contributed_resource_group.add_edge(award_group_node, resource_group_node)
G_contributed_resource_group.add_edge(award_group_node, last_node)
G_contributed_resource_group.add_edge(support_description_node, support_description_node)
G_contributed_resource_group.add_edge(support_description_node, resource_group_node)
G_contributed_resource_group.add_edge(support_description_node, last_node)
G_contributed_resource_group.add_edge(resource_group_node, resource_group_node)
G_contributed_resource_group.add_edge(resource_group_node, last_node)