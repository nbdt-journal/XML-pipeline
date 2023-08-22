import networkx as nx

class Private_char:
    def __init__(self):
        self.name = 'private-char' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('inline-graphic')
        G.add_node('glyph-data')
        G.add_node('glyph-ref')
        #adding edges
        G.add_edge('start', 'inline-graphic')
        G.add_edge('start', 'glyph-data')
        G.add_edge('start', 'glyph-ref')
        G.add_edge('start', 'accept')
        G.add_edge('inline-graphic', 'inline-graphic')
        G.add_edge('inline-graphic', 'accept')
        G.add_edge('glyph-data', 'accept')
        G.add_edge('glyph-ref', 'accept')
        return G