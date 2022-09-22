import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Standards Organization ''' 
# Defining Elements
std_organization = Element('std_organization')
# Creating the Nodes
std_organization_node = Node(element=std_organization, graph=node.get_leaf_graph())
