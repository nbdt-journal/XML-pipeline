import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for named-content ''' 
# Defining Elements
named_content = Element('named-content')
# Creating the Nodes
named_content_node = Node(element=named_content, graph=node.get_leaf_graph())