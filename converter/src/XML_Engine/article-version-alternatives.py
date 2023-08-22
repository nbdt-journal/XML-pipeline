import networkx as nx

class Article_version_alternatives:
    def __init__(self):
        self.name = 'article-version-alternatives' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('article-version')
        #adding edges
        G.add_edge('start', 'article-version')
        G.add_edge('article-version', 'article-version')
        G.add_edge('article-version', 'accept')
        return G