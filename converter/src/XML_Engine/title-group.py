import networkx as nx

class Title_group:
    def __init__(self):
        self.name = 'title-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('article-title')
        G.add_node('subtitle')
        G.add_node('trans-title-group')
        G.add_node('alt-title')
        G.add_node('fn-group')
        #adding edges
        G.add_edge('start', 'article-title')
        G.add_edge('article-title', 'subtitle')
        G.add_edge('article-title', 'trans-title-group')
        G.add_edge('article-title', 'alt-title')
        G.add_edge('article-title', 'fn-group')
        G.add_edge('article-title', 'accept')
        G.add_edge('subtitle', 'subtitle')
        G.add_edge('subtitle', 'trans-title-group')
        G.add_edge('subtitle', 'alt-title')
        G.add_edge('subtitle', 'fn-group')
        G.add_edge('subtitle', 'accept')
        G.add_edge('trans-title-group', 'trans-title-group')
        G.add_edge('trans-title-group', 'alt-title')
        G.add_edge('trans-title-group', 'fn-group')
        G.add_edge('trans-title-group', 'accept')
        G.add_edge('alt-title', 'alt-title')
        G.add_edge('alt-title', 'fn-group')
        G.add_edge('alt-title', 'accept')
        return G