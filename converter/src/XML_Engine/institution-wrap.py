import networkx as nx

class Institution_wrap:
    def __init__(self):
        self.name = 'institution-wrap' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('institution')
        G.add_node('institution-id')
        #adding edges
        G.add_edge('start', 'institution')
        G.add_edge('start', 'institution-id')
        G.add_edge('start', 'accept')
        G.add_edge('institution', 'accept')
        G.add_edge('institution-id', 'accept')
        return G