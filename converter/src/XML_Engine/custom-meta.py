import networkx as nx

class Custom_meta:
    def __init__(self):
        self.name = 'custom-meta' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('meta-name')
        G.add_node('meta-value')
        #adding edges
        G.add_edge('start', 'meta-name')
        G.add_edge('meta-name', 'meta-value')
        G.add_edge('meta-value', 'accept')
        return G