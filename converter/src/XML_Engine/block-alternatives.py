import networkx as nx

class Block_alternatives:
    def __init__(self):
        self.name = 'block-alternatives' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('object-id')
        G.add_node('boxed-text')
        G.add_node('fig')
        G.add_node('fig-group')
        G.add_node('table-wrap')
        G.add_node('table-wrap-group')
        #adding edges
        G.add_edge('start', 'object-id')
        G.add_edge('start', 'accept')
        G.add_edge('object-id', 'boxed-text')
        G.add_edge('object-id', 'fig')
        G.add_edge('object-id', 'fig-group')
        G.add_edge('object-id', 'table-wrap')
        G.add_edge('object-id', 'table-wrap-group')
        G.add_edge('object-id', 'accept')
        G.add_edge('boxed-text', 'accept')
        G.add_edge('fig', 'accept')
        G.add_edge('fig-group', 'accept')
        G.add_edge('table-wrap', 'accept')
        G.add_edge('table-wrap-group', 'accept')
        return G