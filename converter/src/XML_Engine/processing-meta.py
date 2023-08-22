import networkx as nx

class Processing_meta:
    def __init__(self):
        self.name = 'processing-meta' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('restricted-by')
        G.add_node('extended-by')
        G.add_node('custom-meta-group')
        #adding edges
        G.add_edge('start', 'restricted-by')
        G.add_edge('restricted-by', 'restricted-by')
        G.add_edge('restricted-by', 'extended-by')
        G.add_edge('restricted-by', 'custom-meta-group')
        G.add_edge('restricted-by', 'accept')
        G.add_edge('extended-by', 'extended-by')
        G.add_edge('extended-by', 'custom-meta-group')
        G.add_edge('extended-by', 'accept')
        G.add_edge('custom-meta-group', 'custom-meta-group')
        G.add_edge('custom-meta-group', 'accept')
        return G