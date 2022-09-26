import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for supplementary-material ''' 
# Defining Elements
supplementary_material = Element('supplementary-material')
# Creating the Nodes
supplementary_material_node = Node(element=supplementary_material, graph=node.get_leaf_graph())