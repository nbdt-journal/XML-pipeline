import networkx as nx

class Caption:
    def __init__(self):
        self.name = 'caption' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('title')
        G.add_node('p')
        #adding edges
        G.add_edge('start', 'title')
        G.add_edge('title', 'accept')
        G.add_edge('title', 'p')
        G.add_edge('p', 'accept')
        return G