import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for time-stamp ''' 
# Defining Elements
time_stamp = Element('time-stamp')
# Creating the Nodes
time_stamp_node = Node(element=time_stamp, graph=node.get_leaf_graph())
