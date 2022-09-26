import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for anonymous ''' 
# Defining Elements
anonymous = Element('anonymous')
G_anonymous = nx.DiGraph()
anonymous_node = Node(element=anonymous, graph=node.get_leaf_graph())
