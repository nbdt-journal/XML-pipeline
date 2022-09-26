import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Journal ID ''' 
# Defining Elements
journal_id = Element('journal-id')
# Creating the Nodes
journal_id_node = Node(element=journal_id, graph=node.get_leaf_graph())
