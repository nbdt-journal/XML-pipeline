import networkx as nx

class Ali_free_to_read:
    def __init__(self):
        self.name = 'ali:free_to_read' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        #adding edges
        G.add_edge('start', 'accept')
        return G