import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for tex-math ''' 
# Defining Elements
tex_math = Element('tex-math')
# Creating the Nodes
tex_math_node = Node(element=tex_math, graph=node.get_leaf_graph())
