import networkx as nx

class Open_access:
    def __init__(self):
        self.name = 'open-access' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('p')
        #adding edges
        G.add_edge('start', 'p')
        G.add_edge('p', 'accept')
        return G