import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for era ''' 
# Defining Elements
era = Element('era')
# Creating the Nodes
era_node = Node(element=era, graph=node.get_leaf_graph())