import networkx as nx

class Chem_struct_wrap:
    def __init__(self):
        self.name = 'chem-struct-wrap' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('alternatives')
        G.add_node('chem-struct')
        G.add_node('code')
        G.add_node('graphic')
        G.add_node('media')
        G.add_node('preformat')
        G.add_node('textual-form')
        G.add_node('alt-text')
        G.add_node('long-desc')
        G.add_node('email')
        G.add_node('ext-link')
        G.add_node('uri')
        G.add_node('subj-group')
        G.add_node('kwd-group')
        G.add_node('abstract')
        G.add_node('caption')
        G.add_node('object-id')
        G.add_node('attrib')
        G.add_node('permissions')
        #adding edges
        G.add_edge('start', 'accept')
        G.add_edge('start', 'alternatives')
        G.add_edge('start', 'chem-struct')
        G.add_edge('start', 'code')
        G.add_edge('start', 'graphic')
        G.add_edge('start', 'media')
        G.add_edge('start', 'preformat')
        G.add_edge('start', 'textual-form')
        G.add_edge('start', 'object-id')
        G.add_edge('start', 'attrib')
        G.add_edge('start', 'permissions')
        G.add_edge('label', 'alternatives')
        G.add_edge('label', 'chem-struct')
        G.add_edge('label', 'code')
        G.add_edge('label', 'graphic')
        G.add_edge('label', 'media')
        G.add_edge('label', 'preformat')
        G.add_edge('label', 'textual-form')
        G.add_edge('label', 'accept')
        G.add_edge('label', 'alt-text')
        G.add_edge('label', 'long-desc')
        G.add_edge('label', 'email')
        G.add_edge('label', 'ext-link')
        G.add_edge('label', 'uri')
        G.add_edge('label', 'subj-group')
        G.add_edge('label', 'kwd-group')
        G.add_edge('label', 'abstract')
        G.add_edge('label', 'caption')
        G.add_edge('alternatives', 'accept')
        G.add_edge('alternatives', 'attrib')
        G.add_edge('alternatives', 'permissions')
        G.add_edge('chem-struct', 'accept')
        G.add_edge('chem-struct', 'attrib')
        G.add_edge('chem-struct', 'permissions')
        G.add_edge('code', 'accept')
        G.add_edge('code', 'attrib')
        G.add_edge('code', 'permissions')
        G.add_edge('graphic', 'accept')
        G.add_edge('graphic', 'attrib')
        G.add_edge('graphic', 'permissions')
        G.add_edge('media', 'accept')
        G.add_edge('media', 'attrib')
        G.add_edge('media', 'permissions')
        G.add_edge('preformat', 'accept')
        G.add_edge('preformat', 'attrib')
        G.add_edge('preformat', 'permissions')
        G.add_edge('textual-form', 'accept')
        G.add_edge('textual-form', 'attrib')
        G.add_edge('textual-form', 'permissions')
        G.add_edge('alt-text', 'alternatives')
        G.add_edge('alt-text', 'chem-struct')
        G.add_edge('alt-text', 'code')
        G.add_edge('alt-text', 'graphic')
        G.add_edge('alt-text', 'media')
        G.add_edge('alt-text', 'preformat')
        G.add_edge('alt-text', 'textual-form')
        G.add_edge('alt-text', 'accept')
        G.add_edge('long-desc', 'alternatives')
        G.add_edge('long-desc', 'chem-struct')
        G.add_edge('long-desc', 'code')
        G.add_edge('long-desc', 'graphic')
        G.add_edge('long-desc', 'media')
        G.add_edge('long-desc', 'preformat')
        G.add_edge('long-desc', 'textual-form')
        G.add_edge('long-desc', 'accept')
        G.add_edge('email', 'alternatives')
        G.add_edge('email', 'chem-struct')
        G.add_edge('email', 'code')
        G.add_edge('email', 'graphic')
        G.add_edge('email', 'media')
        G.add_edge('email', 'preformat')
        G.add_edge('email', 'textual-form')
        G.add_edge('email', 'accept')
        G.add_edge('ext-link', 'alternatives')
        G.add_edge('ext-link', 'chem-struct')
        G.add_edge('ext-link', 'code')
        G.add_edge('ext-link', 'graphic')
        G.add_edge('ext-link', 'media')
        G.add_edge('ext-link', 'preformat')
        G.add_edge('ext-link', 'textual-form')
        G.add_edge('ext-link', 'accept')
        G.add_edge('uri', 'alternatives')
        G.add_edge('uri', 'chem-struct')
        G.add_edge('uri', 'code')
        G.add_edge('uri', 'graphic')
        G.add_edge('uri', 'media')
        G.add_edge('uri', 'preformat')
        G.add_edge('uri', 'textual-form')
        G.add_edge('uri', 'accept')
        G.add_edge('subj-group', 'alternatives')
        G.add_edge('subj-group', 'chem-struct')
        G.add_edge('subj-group', 'code')
        G.add_edge('subj-group', 'graphic')
        G.add_edge('subj-group', 'media')
        G.add_edge('subj-group', 'preformat')
        G.add_edge('subj-group', 'textual-form')
        G.add_edge('subj-group', 'accept')
        G.add_edge('subj-group', 'alt-text')
        G.add_edge('subj-group', 'long-desc')
        G.add_edge('subj-group', 'email')
        G.add_edge('subj-group', 'ext-link')
        G.add_edge('subj-group', 'uri')
        G.add_edge('kwd-group', 'alternatives')
        G.add_edge('kwd-group', 'chem-struct')
        G.add_edge('kwd-group', 'code')
        G.add_edge('kwd-group', 'graphic')
        G.add_edge('kwd-group', 'media')
        G.add_edge('kwd-group', 'preformat')
        G.add_edge('kwd-group', 'textual-form')
        G.add_edge('kwd-group', 'accept')
        G.add_edge('kwd-group', 'alt-text')
        G.add_edge('kwd-group', 'long-desc')
        G.add_edge('kwd-group', 'email')
        G.add_edge('kwd-group', 'ext-link')
        G.add_edge('kwd-group', 'uri')
        G.add_edge('kwd-group', 'subj-group')
        G.add_edge('abstract', 'alternatives')
        G.add_edge('abstract', 'chem-struct')
        G.add_edge('abstract', 'code')
        G.add_edge('abstract', 'graphic')
        G.add_edge('abstract', 'media')
        G.add_edge('abstract', 'preformat')
        G.add_edge('abstract', 'textual-form')
        G.add_edge('abstract', 'accept')
        G.add_edge('abstract', 'alt-text')
        G.add_edge('abstract', 'long-desc')
        G.add_edge('abstract', 'email')
        G.add_edge('abstract', 'ext-link')
        G.add_edge('abstract', 'uri')
        G.add_edge('abstract', 'subj-group')
        G.add_edge('abstract', 'kwd-group')
        G.add_edge('caption', 'alternatives')
        G.add_edge('caption', 'chem-struct')
        G.add_edge('caption', 'code')
        G.add_edge('caption', 'graphic')
        G.add_edge('caption', 'media')
        G.add_edge('caption', 'preformat')
        G.add_edge('caption', 'textual-form')
        G.add_edge('caption', 'accept')
        G.add_edge('caption', 'alt-text')
        G.add_edge('caption', 'long-desc')
        G.add_edge('caption', 'email')
        G.add_edge('caption', 'ext-link')
        G.add_edge('caption', 'uri')
        G.add_edge('caption', 'subj-group')
        G.add_edge('caption', 'kwd-group')
        G.add_edge('caption', 'abstract')
        G.add_edge('object-id', 'label')
        G.add_edge('object-id', 'alternatives')
        G.add_edge('object-id', 'chem-struct')
        G.add_edge('object-id', 'code')
        G.add_edge('object-id', 'graphic')
        G.add_edge('object-id', 'media')
        G.add_edge('object-id', 'preformat')
        G.add_edge('object-id', 'textual-form')
        G.add_edge('object-id', 'accept')
        G.add_edge('object-id', 'alt-text')
        G.add_edge('object-id', 'long-desc')
        G.add_edge('object-id', 'email')
        G.add_edge('object-id', 'ext-link')
        G.add_edge('object-id', 'uri')
        G.add_edge('object-id', 'subj-group')
        G.add_edge('object-id', 'kwd-group')
        G.add_edge('object-id', 'abstract')
        G.add_edge('object-id', 'caption')
        G.add_edge('attrib', 'accept')
        G.add_edge('permissions', 'accept')
        return G