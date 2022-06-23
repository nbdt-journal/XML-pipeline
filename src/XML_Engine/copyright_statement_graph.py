import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Copyright Statement ''' 
# Defining Elements
copyright_statement = Element('copyright-statement')
# Creating the Nodes
copyright_statement_node = Node(element=copyright_statement, graph=node.get_leaf_graph())
