import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for season ''' 
# Defining Elements
season = Element('season')
# Creating the Nodes
season_node = Node(element=season, graph=node.get_leaf_graph())
