import networkx as nx

class License:
    def __init__(self):
        self.name = 'license' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('ali:license_ref')
        G.add_node('license-p')
        #adding edges
        G.add_edge('start', 'ali:license_ref')
        G.add_edge('start', 'license-p')
        G.add_edge('start', 'accept')
        G.add_edge('ali:license_ref', 'accept')
        G.add_edge('license-p', 'accept')
        return G