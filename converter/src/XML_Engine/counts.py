import networkx as nx

class Counts:
    def __init__(self):
        self.name = 'counts' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('count')
        G.add_node('fig-count')
        G.add_node('table-count')
        G.add_node('equation-count')
        G.add_node('ref-count')
        G.add_node('page-count')
        G.add_node('word-count')
        #adding edges
        G.add_edge('start', 'count')
        G.add_edge('count', 'count')
        G.add_edge('count', 'fig-count')
        G.add_edge('count', 'table-count')
        G.add_edge('count', 'equation-count')
        G.add_edge('count', 'ref-count')
        G.add_edge('count', 'page-count')
        G.add_edge('count', 'word-count')
        G.add_edge('count', 'accept')
        G.add_edge('fig-count', 'table-count')
        G.add_edge('fig-count', 'equation-count')
        G.add_edge('fig-count', 'ref-count')
        G.add_edge('fig-count', 'page-count')
        G.add_edge('fig-count', 'word-count')
        G.add_edge('fig-count', 'accept')
        G.add_edge('table-count', 'equation-count')
        G.add_edge('table-count', 'ref-count')
        G.add_edge('table-count', 'page-count')
        G.add_edge('table-count', 'word-count')
        G.add_edge('table-count', 'accept')
        G.add_edge('equation-count', 'ref-count')
        G.add_edge('equation-count', 'page-count')
        G.add_edge('equation-count', 'word-count')
        G.add_edge('equation-count', 'accept')
        G.add_edge('ref-count', 'page-count')
        G.add_edge('ref-count', 'word-count')
        G.add_edge('ref-count', 'accept')
        G.add_edge('page-count', 'word-count')
        G.add_edge('page-count', 'accept')
        return G