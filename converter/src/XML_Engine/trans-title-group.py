import networkx as nx

class Trans_title_group:
    def __init__(self):
        self.name = 'trans-title-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('trans-title')
        G.add_node('trans-subtitle')
        #adding edges
        G.add_edge('start', 'trans-title')
        G.add_edge('trans-title', 'trans-subtitle')
        G.add_edge('trans-title', 'accept')
        G.add_edge('trans-subtitle', 'trans-subtitle')
        G.add_edge('trans-subtitle', 'accept')
        return G