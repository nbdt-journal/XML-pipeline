import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for principal-award-recipient ''' 
# Defining Elements
principal_award_recipient = Element('principal-award-recipient')
# Creating the Nodes
principal_award_recipient_node = Node(element=principal_award_recipient, graph=node.get_leaf_graph())
