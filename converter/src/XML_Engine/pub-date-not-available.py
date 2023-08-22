import networkx as nx

class Pub_date_not_available:
    def __init__(self):
        self.name = 'pub-date-not-available' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        #adding edges
        G.add_edge('start', 'accept')
        return G