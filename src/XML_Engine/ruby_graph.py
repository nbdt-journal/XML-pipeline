import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for ruby ''' 
# Defining Elements
ruby = Element('ruby')
G_ruby = nx.DiGraph()
# Creating the Nodes
ruby_node = Node(element=ruby, graph=G_ruby)
first_node = node.get_first_node()
last_node = node.get_last_node()
G_ruby.add_nodes_from([first_node, last_node, rb_node, rt_node])
G_ruby.add_edge(first_node, rb_node)
G_ruby.add_edge(rb_node, rt_node)
G_ruby.add_edge(rt_node, last_node)