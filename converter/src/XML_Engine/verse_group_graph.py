import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for verse-group ''' 
# Defining Elements
verse_group = Element('verse-group')
# Creating the Nodes
verse_group_node = Node(element=verse_group, graph=node.get_leaf_graph())