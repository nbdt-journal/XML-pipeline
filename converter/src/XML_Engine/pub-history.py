import networkx as nx

class Pub_history:
    def __init__(self):
        self.name = 'pub-history' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('event')
        #adding edges
        G.add_edge('start', 'event')
        G.add_edge('event', 'accept')
        return G