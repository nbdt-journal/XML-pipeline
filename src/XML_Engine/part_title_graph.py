import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for part-title ''' 
# Defining Elements
part_title = Element('part-title')
# Creating the Nodes
part_title_node = Node(element=part_title, graph=node.get_leaf_graph())