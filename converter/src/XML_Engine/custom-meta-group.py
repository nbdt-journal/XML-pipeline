import networkx as nx

class Custom_meta_group:
    def __init__(self):
        self.name = 'custom-meta-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('custom-meta')
        #adding edges
        G.add_edge('start', 'custom-meta')
        G.add_edge('custom-meta', 'custom-meta')
        G.add_edge('custom-meta', 'accept')
        return G