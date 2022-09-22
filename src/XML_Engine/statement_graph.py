import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Statement ''' 
# Defining Elements
statement = Element('statement')
# Creating the Nodes
statement_node = Node(element=statement, graph=node.get_leaf_graph())
