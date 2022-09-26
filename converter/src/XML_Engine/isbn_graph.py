import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Isbn ''' 
# Defining Elements
isbn = Element('isbn')
# Creating the Nodes
isbn_node = Node(element=isbn, graph=node.get_leaf_graph())