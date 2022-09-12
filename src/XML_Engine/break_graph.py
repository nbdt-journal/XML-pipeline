import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for break ''' 
# Defining Elements
_break = Element('break')
# Creating the Nodes
break_node = Node(element=_break, graph=node.get_leaf_graph())
