import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for styled-content ''' 
# Defining Elements
styled_content = Element('styled-content')
# Creating the Nodes
styled_content_node = Node(element=styled_content, graph=node.get_leaf_graph())
