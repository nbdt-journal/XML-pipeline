import networkx as nx

class Ruby:
    def __init__(self):
        self.name = 'ruby' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('rb')
        G.add_node('rt')
        G.add_node('rp')
        #adding edges
        G.add_edge('start', 'rb')
        G.add_edge('start', 'accept')
        G.add_edge('rb', 'rt')
        G.add_edge('rb', 'accept')
        G.add_edge('rb', 'rp')
        G.add_edge('rt', 'accept')
        return G