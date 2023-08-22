import networkx as nx

class Article:
    def __init__(self):
        self.name = 'article' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('processing-meta')
        G.add_node('front')
        G.add_node('body')
        G.add_node('back')
        G.add_node('floats-group')
        G.add_node('sub-article')
        G.add_node('response')
        #adding edges
        G.add_edge('start', 'processing-meta')
        G.add_edge('processing-meta', 'front')
        G.add_edge('front', 'body')
        G.add_edge('front', 'back')
        G.add_edge('front', 'floats-group')
        G.add_edge('front', 'sub-article')
        G.add_edge('body', 'back')
        G.add_edge('body', 'floats-group')
        G.add_edge('body', 'sub-article')
        G.add_edge('back', 'floats-group')
        G.add_edge('back', 'sub-article')
        G.add_edge('floats-group', 'sub-article')
        G.add_edge('sub-article', 'accept')
        G.add_edge('response', 'accept')
        return G