import networkx as nx

class Colgroup:
    def __init__(self):
        self.name = 'colgroup' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('col')
        #adding edges
        G.add_edge('start', 'col')
        G.add_edge('col', 'accept')
        return G