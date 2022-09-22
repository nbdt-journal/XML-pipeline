import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for patent ''' 
# Defining Elements
patent = Element('patent')
# Creating the Nodes
patent_node = Node(element=patent, graph=node.get_leaf_graph())
