import networkx as nx

class Ref:
    def __init__(self):
        self.name = 'ref' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('citation-alternatives')
        G.add_node('element-citation')
        G.add_node('mixed-citation')
        G.add_node('nlm-citation')
        G.add_node('note')
        G.add_node('x')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('label', 'citation-alternatives')
        G.add_edge('label', 'element-citation')
        G.add_edge('label', 'mixed-citation')
        G.add_edge('label', 'nlm-citation')
        G.add_edge('label', 'note')
        G.add_edge('label', 'x')
        G.add_edge('label', 'accept')
        G.add_edge('citation-alternatives', 'accept')
        G.add_edge('element-citation', 'accept')
        G.add_edge('mixed-citation', 'accept')
        G.add_edge('nlm-citation', 'accept')
        G.add_edge('note', 'accept')
        G.add_edge('x', 'accept')
        return G