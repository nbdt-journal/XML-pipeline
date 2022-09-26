import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Publication Identifier ''' 
# Defining Elements
pub_id = Element('pub-id')
# Creating the Nodes
pub_id_node = Node(element=pub_id, graph=node.get_leaf_graph())
