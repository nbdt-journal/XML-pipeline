import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for award-name ''' 
# Defining Elements
award_name = Element('award-name')
# Creating the Nodes
award_name_node = Node(element=award_name, graph=node.get_leaf_graph())
