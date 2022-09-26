import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for award-desc ''' 
# Defining Elements
award_desc = Element('award-desc')
# Creating the Nodes
award_desc_node = Node(element=award_desc, graph=node.get_leaf_graph())