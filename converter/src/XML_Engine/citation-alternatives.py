import networkx as nx

class Citation_alternatives:
    def __init__(self):
        self.name = 'citation-alternatives' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('object-id')
        G.add_node('element-citation')
        G.add_node('mixed-citation')
        G.add_node('nlm-citation')
        #adding edges
        G.add_edge('start', 'object-id')
        G.add_edge('start', 'accept')
        G.add_edge('object-id', 'element-citation')
        G.add_edge('object-id', 'mixed-citation')
        G.add_edge('object-id', 'nlm-citation')
        G.add_edge('object-id', 'accept')
        G.add_edge('element-citation', 'accept')
        G.add_edge('mixed-citation', 'accept')
        G.add_edge('nlm-citation', 'accept')
        return G