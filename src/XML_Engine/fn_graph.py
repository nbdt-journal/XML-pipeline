import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for FN ''' 
# Defining Elements
fn = Element('fn')
# Creating the Nodes
fn_node = Node(element=fn, graph=node.get_leaf_graph())