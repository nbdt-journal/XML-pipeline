import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for funding-group ''' 
# Defining Elements
funding_group = Element('funding-group')
# Creating the Nodes
funding_group_node = Node(element=funding_group, graph=node.get_leaf_graph())