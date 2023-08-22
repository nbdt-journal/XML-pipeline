import networkx as nx

class Response:
    def __init__(self):
        self.name = 'response' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('processing-meta')
        G.add_node('body')
        G.add_node('back')
        G.add_node('floats-group')
        G.add_node('front')
        G.add_node('front-stub')
        #adding edges
        G.add_edge('start', 'processing-meta')
        G.add_edge('start', 'body')
        G.add_edge('start', 'back')
        G.add_edge('start', 'floats-group')
        G.add_edge('start', 'accept')
        G.add_edge('processing-meta', 'front')
        G.add_edge('processing-meta', 'front-stub')
        G.add_edge('processing-meta', 'accept')
        G.add_edge('body', 'back')
        G.add_edge('body', 'floats-group')
        G.add_edge('body', 'accept')
        G.add_edge('back', 'floats-group')
        G.add_edge('back', 'accept')
        G.add_edge('front', 'body')
        G.add_edge('front', 'back')
        G.add_edge('front', 'floats-group')
        G.add_edge('front', 'accept')
        G.add_edge('front-stub', 'body')
        G.add_edge('front-stub', 'back')
        G.add_edge('front-stub', 'floats-group')
        G.add_edge('front-stub', 'accept')
        return G