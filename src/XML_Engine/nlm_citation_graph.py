import networkx as nx 

import node
from node import Node 
from element import Element 

#This element is deprecated. Avoid using it; use <element-citation>

''' Building a graph for nlm-citation ''' 
# Defining Elements
nlm_citation = Element('nlm-citation')
# Creating the Nodes
nlm_citation_node = Node(element=nlm_citation, graph=node.get_leaf_graph())