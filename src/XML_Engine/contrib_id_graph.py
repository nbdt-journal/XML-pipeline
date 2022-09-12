import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for contrib-id ''' 
# Defining Elements
contrib_id = Element('contrib-id')
# Creating the Nodes
contrib_id_node = Node(element=contrib_id, graph=node.get_leaf_graph())