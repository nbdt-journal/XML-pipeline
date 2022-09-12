import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for conf-acronym ''' 
# Defining Elements
conf_acronym = Element('conf-acronym')
# Creating the Nodes
conf_acronym_node = Node(element=conf_acronym, graph=node.get_leaf_graph())