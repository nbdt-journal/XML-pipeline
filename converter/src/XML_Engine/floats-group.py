import networkx as nx

class Floats_group:
    def __init__(self):
        self.name = 'floats-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('alternatives')
        G.add_node('block-alternatives')
        G.add_node('boxed-text')
        G.add_node('chem-struct-wrap')
        G.add_node('code')
        G.add_node('fig')
        G.add_node('fig-group')
        G.add_node('graphic')
        G.add_node('media')
        G.add_node('preformat')
        G.add_node('supplementary-material')
        G.add_node('table-wrap')
        G.add_node('table-wrap-group')
        #adding edges
        G.add_edge('start', 'alternatives')
        G.add_edge('start', 'block-alternatives')
        G.add_edge('start', 'boxed-text')
        G.add_edge('start', 'chem-struct-wrap')
        G.add_edge('start', 'code')
        G.add_edge('start', 'fig')
        G.add_edge('start', 'fig-group')
        G.add_edge('start', 'graphic')
        G.add_edge('start', 'media')
        G.add_edge('start', 'preformat')
        G.add_edge('start', 'supplementary-material')
        G.add_edge('start', 'table-wrap')
        G.add_edge('start', 'table-wrap-group')
        G.add_edge('start', 'accept')
        G.add_edge('alternatives', 'accept')
        G.add_edge('block-alternatives', 'accept')
        G.add_edge('boxed-text', 'accept')
        G.add_edge('chem-struct-wrap', 'accept')
        G.add_edge('code', 'accept')
        G.add_edge('fig', 'accept')
        G.add_edge('fig-group', 'accept')
        G.add_edge('graphic', 'accept')
        G.add_edge('media', 'accept')
        G.add_edge('preformat', 'accept')
        G.add_edge('supplementary-material', 'accept')
        G.add_edge('table-wrap', 'accept')
        G.add_edge('table-wrap-group', 'accept')
        return G