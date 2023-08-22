import networkx as nx

class Inline_graphic:
    def __init__(self):
        self.name = 'inline-graphic' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('alt-text')
        G.add_node('long-desc')
        #adding edges
        G.add_edge('start', 'alt-text')
        G.add_edge('start', 'long-desc')
        G.add_edge('start', 'accept')
        G.add_edge('alt-text', 'accept')
        G.add_edge('long-desc', 'accept')
        return G