import networkx as nx

class Verse_group:
    def __init__(self):
        self.name = 'verse-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('title')
        G.add_node('subtitle')
        G.add_node('verse-line')
        G.add_node('verse-group')
        G.add_node('attrib')
        G.add_node('permissions')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('start', 'attrib')
        G.add_edge('start', 'permissions')
        G.add_edge('label', 'title')
        G.add_edge('label', 'subtitle')
        G.add_edge('label', 'verse-line')
        G.add_edge('label', 'verse-group')
        G.add_edge('label', 'accept')
        G.add_edge('title', 'subtitle')
        G.add_edge('title', 'verse-line')
        G.add_edge('title', 'verse-group')
        G.add_edge('title', 'accept')
        G.add_edge('subtitle', 'verse-line')
        G.add_edge('subtitle', 'verse-group')
        G.add_edge('subtitle', 'accept')
        G.add_edge('verse-line', 'accept')
        G.add_edge('verse-line', 'attrib')
        G.add_edge('verse-line', 'permissions')
        G.add_edge('verse-group', 'accept')
        G.add_edge('verse-group', 'attrib')
        G.add_edge('verse-group', 'permissions')
        G.add_edge('attrib', 'accept')
        G.add_edge('permissions', 'accept')
        return G