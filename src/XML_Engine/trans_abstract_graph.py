import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for trans-abstract ''' 
# Defining Elements
trans_abstract = Element('trans-abstract')
# Creating the Nodes
trans_abstract_node = Node(element=trans_abstract, graph=node.get_leaf_graph())