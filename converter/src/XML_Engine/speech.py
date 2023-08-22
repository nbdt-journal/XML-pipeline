import networkx as nx

class Speech:
    def __init__(self):
        self.name = 'speech' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('speaker')
        G.add_node('object-id')
        G.add_node('p')
        #adding edges
        G.add_edge('start', 'object-id')
        G.add_edge('speaker', 'p')
        G.add_edge('object-id', 'speaker')
        G.add_edge('p', 'accept')
        return G