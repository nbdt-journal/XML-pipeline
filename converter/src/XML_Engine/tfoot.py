import networkx as nx

class Tfoot:
    def __init__(self):
        self.name = 'tfoot' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('tr')
        #adding edges
        G.add_edge('start', 'tr')
        G.add_edge('tr', 'accept')
        return G