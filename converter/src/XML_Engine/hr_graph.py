import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for hr ''' 
# Defining Elements
hr = Element('hr')
# Creating the Nodes
hr_node = Node(element=hr, graph=node.get_leaf_graph())