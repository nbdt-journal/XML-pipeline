import networkx as nx

class Front:
    def __init__(self):
        self.name = 'front' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('journal-meta')
        G.add_node('article-meta')
        G.add_node('def-list')
        G.add_node('list')
        G.add_node('ack')
        G.add_node('bio')
        G.add_node('fn-group')
        G.add_node('glossary')
        G.add_node('notes')
        #adding edges
        G.add_edge('start', 'journal-meta')
        G.add_edge('start', 'accept')
        G.add_edge('journal-meta', 'article-meta')
        G.add_edge('article-meta', 'accept')
        G.add_edge('article-meta', 'def-list')
        G.add_edge('article-meta', 'list')
        G.add_edge('article-meta', 'ack')
        G.add_edge('article-meta', 'bio')
        G.add_edge('article-meta', 'fn-group')
        G.add_edge('article-meta', 'glossary')
        G.add_edge('article-meta', 'notes')
        G.add_edge('def-list', 'accept')
        G.add_edge('list', 'accept')
        G.add_edge('ack', 'accept')
        G.add_edge('bio', 'accept')
        G.add_edge('fn-group', 'accept')
        G.add_edge('glossary', 'accept')
        G.add_edge('notes', 'accept')
        return G