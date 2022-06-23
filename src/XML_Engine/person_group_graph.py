import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Person Group ''' 
# Defining Elements
person_group = Element('person-group')
# Creating the Nodes
person_group_node = Node(element=person_group, graph=node.get_leaf_graph())
