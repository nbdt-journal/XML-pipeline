import networkx as nx

class Table_wrap_group:
    def __init__(self):
        self.name = 'table-wrap-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('alt-text')
        G.add_node('long-desc')
        G.add_node('email')
        G.add_node('ext-link')
        G.add_node('uri')
        G.add_node('subj-group')
        G.add_node('kwd-group')
        G.add_node('abstract')
        G.add_node('caption')
        G.add_node('label')
        G.add_node('object-id')
        G.add_node('table-wrap')
        G.add_node('xref')
        #adding edges
        G.add_edge('start', 'object-id')
        G.add_edge('start', 'table-wrap')
        G.add_edge('start', 'xref')
        G.add_edge('start', 'accept')
        G.add_edge('alt-text', 'table-wrap')
        G.add_edge('alt-text', 'xref')
        G.add_edge('alt-text', 'accept')
        G.add_edge('long-desc', 'table-wrap')
        G.add_edge('long-desc', 'xref')
        G.add_edge('long-desc', 'accept')
        G.add_edge('email', 'table-wrap')
        G.add_edge('email', 'xref')
        G.add_edge('email', 'accept')
        G.add_edge('ext-link', 'table-wrap')
        G.add_edge('ext-link', 'xref')
        G.add_edge('ext-link', 'accept')
        G.add_edge('uri', 'table-wrap')
        G.add_edge('uri', 'xref')
        G.add_edge('uri', 'accept')
        G.add_edge('subj-group', 'alt-text')
        G.add_edge('subj-group', 'long-desc')
        G.add_edge('subj-group', 'email')
        G.add_edge('subj-group', 'ext-link')
        G.add_edge('subj-group', 'uri')
        G.add_edge('subj-group', 'accept')
        G.add_edge('subj-group', 'table-wrap')
        G.add_edge('subj-group', 'xref')
        G.add_edge('kwd-group', 'alt-text')
        G.add_edge('kwd-group', 'long-desc')
        G.add_edge('kwd-group', 'email')
        G.add_edge('kwd-group', 'ext-link')
        G.add_edge('kwd-group', 'uri')
        G.add_edge('kwd-group', 'accept')
        G.add_edge('kwd-group', 'subj-group')
        G.add_edge('kwd-group', 'table-wrap')
        G.add_edge('kwd-group', 'xref')
        G.add_edge('abstract', 'alt-text')
        G.add_edge('abstract', 'long-desc')
        G.add_edge('abstract', 'email')
        G.add_edge('abstract', 'ext-link')
        G.add_edge('abstract', 'uri')
        G.add_edge('abstract', 'accept')
        G.add_edge('abstract', 'subj-group')
        G.add_edge('abstract', 'kwd-group')
        G.add_edge('abstract', 'table-wrap')
        G.add_edge('abstract', 'xref')
        G.add_edge('caption', 'alt-text')
        G.add_edge('caption', 'long-desc')
        G.add_edge('caption', 'email')
        G.add_edge('caption', 'ext-link')
        G.add_edge('caption', 'uri')
        G.add_edge('caption', 'accept')
        G.add_edge('caption', 'subj-group')
        G.add_edge('caption', 'kwd-group')
        G.add_edge('caption', 'abstract')
        G.add_edge('caption', 'table-wrap')
        G.add_edge('caption', 'xref')
        G.add_edge('label', 'alt-text')
        G.add_edge('label', 'long-desc')
        G.add_edge('label', 'email')
        G.add_edge('label', 'ext-link')
        G.add_edge('label', 'uri')
        G.add_edge('label', 'accept')
        G.add_edge('label', 'subj-group')
        G.add_edge('label', 'kwd-group')
        G.add_edge('label', 'abstract')
        G.add_edge('label', 'caption')
        G.add_edge('label', 'table-wrap')
        G.add_edge('label', 'xref')
        G.add_edge('object-id', 'alt-text')
        G.add_edge('object-id', 'long-desc')
        G.add_edge('object-id', 'email')
        G.add_edge('object-id', 'ext-link')
        G.add_edge('object-id', 'uri')
        G.add_edge('object-id', 'accept')
        G.add_edge('object-id', 'subj-group')
        G.add_edge('object-id', 'kwd-group')
        G.add_edge('object-id', 'abstract')
        G.add_edge('object-id', 'caption')
        G.add_edge('object-id', 'label')
        G.add_edge('object-id', 'table-wrap')
        G.add_edge('object-id', 'xref')
        G.add_edge('table-wrap', 'accept')
        G.add_edge('xref', 'accept')
        return G