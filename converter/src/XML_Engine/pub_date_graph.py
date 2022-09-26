import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Pub Date ''' 
# Defining Elements
pub_date = Element('pub-date')
# Creating the Nodes
pub_date_node = Node(element=pub_date, graph=node.get_leaf_graph())