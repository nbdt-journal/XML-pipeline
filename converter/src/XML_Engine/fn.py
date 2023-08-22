import networkx as nx

class Fn:
    def __init__(self):
        self.name = 'fn' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('p')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('label', 'p')
        G.add_edge('p', 'accept')
        return G