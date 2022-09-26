import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for conf-num ''' 
# Defining Elements
conf_num = Element('conf-num')
# Creating the Nodes
conf_num_node = Node(element=conf_num, graph=node.get_leaf_graph())