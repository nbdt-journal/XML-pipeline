import networkx as nx

class Media:
    def __init__(self):
        self.name = 'media' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('alt-text')
        G.add_node('long-desc')
        G.add_node('abstract')
        G.add_node('email')
        G.add_node('ext-link')
        G.add_node('uri')
        G.add_node('caption')
        G.add_node('attrib')
        G.add_node('permissions')
        G.add_node('object-id')
        G.add_node('label')
        G.add_node('kwd-group')
        G.add_node('subj-group')
        G.add_node('xref')
        #adding edges
        G.add_edge('start', 'alt-text')
        G.add_edge('start', 'long-desc')
        G.add_edge('start', 'abstract')
        G.add_edge('start', 'email')
        G.add_edge('start', 'ext-link')
        G.add_edge('start', 'uri')
        G.add_edge('start', 'caption')
        G.add_edge('start', 'attrib')
        G.add_edge('start', 'permissions')
        G.add_edge('start', 'object-id')
        G.add_edge('start', 'label')
        G.add_edge('start', 'kwd-group')
        G.add_edge('start', 'subj-group')
        G.add_edge('start', 'xref')
        G.add_edge('start', 'accept')
        G.add_edge('alt-text', 'accept')
        G.add_edge('long-desc', 'accept')
        G.add_edge('abstract', 'accept')
        G.add_edge('email', 'accept')
        G.add_edge('ext-link', 'accept')
        G.add_edge('uri', 'accept')
        G.add_edge('caption', 'accept')
        G.add_edge('attrib', 'accept')
        G.add_edge('permissions', 'accept')
        G.add_edge('object-id', 'accept')
        G.add_edge('label', 'accept')
        G.add_edge('kwd-group', 'accept')
        G.add_edge('subj-group', 'accept')
        G.add_edge('xref', 'accept')
        return G