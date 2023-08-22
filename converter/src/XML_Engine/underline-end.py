import networkx as nx

class Underline_end:
    def __init__(self):
        self.name = 'underline-end' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        #adding edges
        G.add_edge('start', 'accept')
        return G