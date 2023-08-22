import networkx as nx

class Back:
    def __init__(self):
        self.name = 'back' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('title')
        G.add_node('ack')
        G.add_node('app-group')
        G.add_node('bio')
        G.add_node('fn-group')
        G.add_node('glossary')
        G.add_node('ref-list')
        G.add_node('notes')
        G.add_node('sec')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('label', 'title')
        G.add_edge('label', 'accept')
        G.add_edge('label', 'ack')
        G.add_edge('label', 'app-group')
        G.add_edge('label', 'bio')
        G.add_edge('label', 'fn-group')
        G.add_edge('label', 'glossary')
        G.add_edge('label', 'ref-list')
        G.add_edge('label', 'notes')
        G.add_edge('label', 'sec')
        G.add_edge('title', 'title')
        G.add_edge('title', 'accept')
        G.add_edge('title', 'ack')
        G.add_edge('title', 'app-group')
        G.add_edge('title', 'bio')
        G.add_edge('title', 'fn-group')
        G.add_edge('title', 'glossary')
        G.add_edge('title', 'ref-list')
        G.add_edge('title', 'notes')
        G.add_edge('title', 'sec')
        G.add_edge('ack', 'accept')
        G.add_edge('app-group', 'accept')
        G.add_edge('bio', 'accept')
        G.add_edge('fn-group', 'accept')
        G.add_edge('glossary', 'accept')
        G.add_edge('ref-list', 'accept')
        G.add_edge('notes', 'accept')
        G.add_edge('sec', 'accept')
        return G