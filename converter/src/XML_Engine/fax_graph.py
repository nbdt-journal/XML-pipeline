import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for fax ''' 
# Defining Elements
fax = Element('fax')
# Creating the Nodes
fax_node = Node(element=fax, graph=node.get_leaf_graph())