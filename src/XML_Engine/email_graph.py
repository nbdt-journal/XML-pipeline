import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for email ''' 
# Defining Elements
email = Element('email')
# Creating the Nodes
email_node = Node(element=email, graph=node.get_leaf_graph())