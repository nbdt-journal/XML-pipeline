import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Abbrev Journal Title ''' 
# Defining Elements
abbrev_journal_title = Element('abbrev-journal-title')
# Creating the Nodes
abbrev_journal_title_node = Node(element=abbrev_journal_title, graph=node.get_leaf_graph())