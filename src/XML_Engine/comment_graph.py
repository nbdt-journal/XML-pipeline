import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Comment ''' 
# Defining Elements
comment = Element('comment')
# Creating the Nodes
comment_node = Node(element=comment, graph=node.get_leaf_graph())
