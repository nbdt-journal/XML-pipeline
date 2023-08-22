import networkx as nx

class Index_term:
    def __init__(self):
        self.name = 'index-term' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('term')
        G.add_node('index-term')
        G.add_node('see')
        G.add_node('see-also')
        #adding edges
        G.add_edge('start', 'term')
        G.add_edge('start', 'accept')
        G.add_edge('term', 'index-term')
        G.add_edge('term', 'see')
        G.add_edge('term', 'see-also')
        G.add_edge('term', 'accept')
        G.add_edge('index-term', 'accept')
        G.add_edge('see', 'accept')
        G.add_edge('see-also', 'accept')
        return G