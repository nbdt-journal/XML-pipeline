import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Compound Subject Part ''' 
# Defining Elements
compound_subject_part = Element('compound-subject-part')
# Creating the Nodes
compound_subject_part_node = Node(element=compound_subject_part, graph=node.get_leaf_graph())