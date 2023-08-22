import networkx as nx

class Fig:
    def __init__(self):
        self.name = 'fig' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('disp-formula')
        G.add_node('disp-formula-group')
        G.add_node('chem-struct-wrap')
        G.add_node('disp-quote')
        G.add_node('speech')
        G.add_node('statement')
        G.add_node('verse-group')
        G.add_node('table-wrap')
        G.add_node('p')
        G.add_node('def-list')
        G.add_node('list')
        G.add_node('alternatives')
        G.add_node('array')
        G.add_node('code')
        G.add_node('graphic')
        G.add_node('media')
        G.add_node('preformat')
        G.add_node('xref')
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
        G.add_node('attrib')
        G.add_node('permissions')
        #adding edges
        G.add_edge('start', 'accept')
        G.add_edge('start', 'disp-formula')
        G.add_edge('start', 'disp-formula-group')
        G.add_edge('start', 'chem-struct-wrap')
        G.add_edge('start', 'disp-quote')
        G.add_edge('start', 'speech')
        G.add_edge('start', 'statement')
        G.add_edge('start', 'verse-group')
        G.add_edge('start', 'table-wrap')
        G.add_edge('start', 'p')
        G.add_edge('start', 'def-list')
        G.add_edge('start', 'list')
        G.add_edge('start', 'alternatives')
        G.add_edge('start', 'array')
        G.add_edge('start', 'code')
        G.add_edge('start', 'graphic')
        G.add_edge('start', 'media')
        G.add_edge('start', 'preformat')
        G.add_edge('start', 'xref')
        G.add_edge('start', 'object-id')
        G.add_edge('start', 'attrib')
        G.add_edge('start', 'permissions')
        G.add_edge('disp-formula', 'accept')
        G.add_edge('disp-formula', 'attrib')
        G.add_edge('disp-formula', 'permissions')
        G.add_edge('disp-formula-group', 'accept')
        G.add_edge('disp-formula-group', 'attrib')
        G.add_edge('disp-formula-group', 'permissions')
        G.add_edge('chem-struct-wrap', 'accept')
        G.add_edge('chem-struct-wrap', 'attrib')
        G.add_edge('chem-struct-wrap', 'permissions')
        G.add_edge('disp-quote', 'accept')
        G.add_edge('disp-quote', 'attrib')
        G.add_edge('disp-quote', 'permissions')
        G.add_edge('speech', 'accept')
        G.add_edge('speech', 'attrib')
        G.add_edge('speech', 'permissions')
        G.add_edge('statement', 'accept')
        G.add_edge('statement', 'attrib')
        G.add_edge('statement', 'permissions')
        G.add_edge('verse-group', 'accept')
        G.add_edge('verse-group', 'attrib')
        G.add_edge('verse-group', 'permissions')
        G.add_edge('table-wrap', 'accept')
        G.add_edge('table-wrap', 'attrib')
        G.add_edge('table-wrap', 'permissions')
        G.add_edge('p', 'accept')
        G.add_edge('p', 'attrib')
        G.add_edge('p', 'permissions')
        G.add_edge('def-list', 'accept')
        G.add_edge('def-list', 'attrib')
        G.add_edge('def-list', 'permissions')
        G.add_edge('list', 'accept')
        G.add_edge('list', 'attrib')
        G.add_edge('list', 'permissions')
        G.add_edge('alternatives', 'accept')
        G.add_edge('alternatives', 'attrib')
        G.add_edge('alternatives', 'permissions')
        G.add_edge('array', 'accept')
        G.add_edge('array', 'attrib')
        G.add_edge('array', 'permissions')
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
        G.add_edge('xref', 'accept')
        G.add_edge('xref', 'attrib')
        G.add_edge('xref', 'permissions')
        G.add_edge('alt-text', 'accept')
        G.add_edge('alt-text', 'disp-formula')
        G.add_edge('alt-text', 'disp-formula-group')
        G.add_edge('alt-text', 'chem-struct-wrap')
        G.add_edge('alt-text', 'disp-quote')
        G.add_edge('alt-text', 'speech')
        G.add_edge('alt-text', 'statement')
        G.add_edge('alt-text', 'verse-group')
        G.add_edge('alt-text', 'table-wrap')
        G.add_edge('alt-text', 'p')
        G.add_edge('alt-text', 'def-list')
        G.add_edge('alt-text', 'list')
        G.add_edge('alt-text', 'alternatives')
        G.add_edge('alt-text', 'array')
        G.add_edge('alt-text', 'code')
        G.add_edge('alt-text', 'graphic')
        G.add_edge('alt-text', 'media')
        G.add_edge('alt-text', 'preformat')
        G.add_edge('alt-text', 'xref')
        G.add_edge('alt-text', 'attrib')
        G.add_edge('alt-text', 'permissions')
        G.add_edge('long-desc', 'accept')
        G.add_edge('long-desc', 'disp-formula')
        G.add_edge('long-desc', 'disp-formula-group')
        G.add_edge('long-desc', 'chem-struct-wrap')
        G.add_edge('long-desc', 'disp-quote')
        G.add_edge('long-desc', 'speech')
        G.add_edge('long-desc', 'statement')
        G.add_edge('long-desc', 'verse-group')
        G.add_edge('long-desc', 'table-wrap')
        G.add_edge('long-desc', 'p')
        G.add_edge('long-desc', 'def-list')
        G.add_edge('long-desc', 'list')
        G.add_edge('long-desc', 'alternatives')
        G.add_edge('long-desc', 'array')
        G.add_edge('long-desc', 'code')
        G.add_edge('long-desc', 'graphic')
        G.add_edge('long-desc', 'media')
        G.add_edge('long-desc', 'preformat')
        G.add_edge('long-desc', 'xref')
        G.add_edge('long-desc', 'attrib')
        G.add_edge('long-desc', 'permissions')
        G.add_edge('email', 'accept')
        G.add_edge('email', 'disp-formula')
        G.add_edge('email', 'disp-formula-group')
        G.add_edge('email', 'chem-struct-wrap')
        G.add_edge('email', 'disp-quote')
        G.add_edge('email', 'speech')
        G.add_edge('email', 'statement')
        G.add_edge('email', 'verse-group')
        G.add_edge('email', 'table-wrap')
        G.add_edge('email', 'p')
        G.add_edge('email', 'def-list')
        G.add_edge('email', 'list')
        G.add_edge('email', 'alternatives')
        G.add_edge('email', 'array')
        G.add_edge('email', 'code')
        G.add_edge('email', 'graphic')
        G.add_edge('email', 'media')
        G.add_edge('email', 'preformat')
        G.add_edge('email', 'xref')
        G.add_edge('email', 'attrib')
        G.add_edge('email', 'permissions')
        G.add_edge('ext-link', 'accept')
        G.add_edge('ext-link', 'disp-formula')
        G.add_edge('ext-link', 'disp-formula-group')
        G.add_edge('ext-link', 'chem-struct-wrap')
        G.add_edge('ext-link', 'disp-quote')
        G.add_edge('ext-link', 'speech')
        G.add_edge('ext-link', 'statement')
        G.add_edge('ext-link', 'verse-group')
        G.add_edge('ext-link', 'table-wrap')
        G.add_edge('ext-link', 'p')
        G.add_edge('ext-link', 'def-list')
        G.add_edge('ext-link', 'list')
        G.add_edge('ext-link', 'alternatives')
        G.add_edge('ext-link', 'array')
        G.add_edge('ext-link', 'code')
        G.add_edge('ext-link', 'graphic')
        G.add_edge('ext-link', 'media')
        G.add_edge('ext-link', 'preformat')
        G.add_edge('ext-link', 'xref')
        G.add_edge('ext-link', 'attrib')
        G.add_edge('ext-link', 'permissions')
        G.add_edge('uri', 'accept')
        G.add_edge('uri', 'disp-formula')
        G.add_edge('uri', 'disp-formula-group')
        G.add_edge('uri', 'chem-struct-wrap')
        G.add_edge('uri', 'disp-quote')
        G.add_edge('uri', 'speech')
        G.add_edge('uri', 'statement')
        G.add_edge('uri', 'verse-group')
        G.add_edge('uri', 'table-wrap')
        G.add_edge('uri', 'p')
        G.add_edge('uri', 'def-list')
        G.add_edge('uri', 'list')
        G.add_edge('uri', 'alternatives')
        G.add_edge('uri', 'array')
        G.add_edge('uri', 'code')
        G.add_edge('uri', 'graphic')
        G.add_edge('uri', 'media')
        G.add_edge('uri', 'preformat')
        G.add_edge('uri', 'xref')
        G.add_edge('uri', 'attrib')
        G.add_edge('uri', 'permissions')
        G.add_edge('subj-group', 'accept')
        G.add_edge('subj-group', 'disp-formula')
        G.add_edge('subj-group', 'disp-formula-group')
        G.add_edge('subj-group', 'chem-struct-wrap')
        G.add_edge('subj-group', 'disp-quote')
        G.add_edge('subj-group', 'speech')
        G.add_edge('subj-group', 'statement')
        G.add_edge('subj-group', 'verse-group')
        G.add_edge('subj-group', 'table-wrap')
        G.add_edge('subj-group', 'p')
        G.add_edge('subj-group', 'def-list')
        G.add_edge('subj-group', 'list')
        G.add_edge('subj-group', 'alternatives')
        G.add_edge('subj-group', 'array')
        G.add_edge('subj-group', 'code')
        G.add_edge('subj-group', 'graphic')
        G.add_edge('subj-group', 'media')
        G.add_edge('subj-group', 'preformat')
        G.add_edge('subj-group', 'xref')
        G.add_edge('subj-group', 'alt-text')
        G.add_edge('subj-group', 'long-desc')
        G.add_edge('subj-group', 'email')
        G.add_edge('subj-group', 'ext-link')
        G.add_edge('subj-group', 'uri')
        G.add_edge('subj-group', 'attrib')
        G.add_edge('subj-group', 'permissions')
        G.add_edge('kwd-group', 'accept')
        G.add_edge('kwd-group', 'disp-formula')
        G.add_edge('kwd-group', 'disp-formula-group')
        G.add_edge('kwd-group', 'chem-struct-wrap')
        G.add_edge('kwd-group', 'disp-quote')
        G.add_edge('kwd-group', 'speech')
        G.add_edge('kwd-group', 'statement')
        G.add_edge('kwd-group', 'verse-group')
        G.add_edge('kwd-group', 'table-wrap')
        G.add_edge('kwd-group', 'p')
        G.add_edge('kwd-group', 'def-list')
        G.add_edge('kwd-group', 'list')
        G.add_edge('kwd-group', 'alternatives')
        G.add_edge('kwd-group', 'array')
        G.add_edge('kwd-group', 'code')
        G.add_edge('kwd-group', 'graphic')
        G.add_edge('kwd-group', 'media')
        G.add_edge('kwd-group', 'preformat')
        G.add_edge('kwd-group', 'xref')
        G.add_edge('kwd-group', 'alt-text')
        G.add_edge('kwd-group', 'long-desc')
        G.add_edge('kwd-group', 'email')
        G.add_edge('kwd-group', 'ext-link')
        G.add_edge('kwd-group', 'uri')
        G.add_edge('kwd-group', 'subj-group')
        G.add_edge('kwd-group', 'attrib')
        G.add_edge('kwd-group', 'permissions')
        G.add_edge('abstract', 'accept')
        G.add_edge('abstract', 'disp-formula')
        G.add_edge('abstract', 'disp-formula-group')
        G.add_edge('abstract', 'chem-struct-wrap')
        G.add_edge('abstract', 'disp-quote')
        G.add_edge('abstract', 'speech')
        G.add_edge('abstract', 'statement')
        G.add_edge('abstract', 'verse-group')
        G.add_edge('abstract', 'table-wrap')
        G.add_edge('abstract', 'p')
        G.add_edge('abstract', 'def-list')
        G.add_edge('abstract', 'list')
        G.add_edge('abstract', 'alternatives')
        G.add_edge('abstract', 'array')
        G.add_edge('abstract', 'code')
        G.add_edge('abstract', 'graphic')
        G.add_edge('abstract', 'media')
        G.add_edge('abstract', 'preformat')
        G.add_edge('abstract', 'xref')
        G.add_edge('abstract', 'alt-text')
        G.add_edge('abstract', 'long-desc')
        G.add_edge('abstract', 'email')
        G.add_edge('abstract', 'ext-link')
        G.add_edge('abstract', 'uri')
        G.add_edge('abstract', 'subj-group')
        G.add_edge('abstract', 'kwd-group')
        G.add_edge('abstract', 'attrib')
        G.add_edge('abstract', 'permissions')
        G.add_edge('caption', 'accept')
        G.add_edge('caption', 'disp-formula')
        G.add_edge('caption', 'disp-formula-group')
        G.add_edge('caption', 'chem-struct-wrap')
        G.add_edge('caption', 'disp-quote')
        G.add_edge('caption', 'speech')
        G.add_edge('caption', 'statement')
        G.add_edge('caption', 'verse-group')
        G.add_edge('caption', 'table-wrap')
        G.add_edge('caption', 'p')
        G.add_edge('caption', 'def-list')
        G.add_edge('caption', 'list')
        G.add_edge('caption', 'alternatives')
        G.add_edge('caption', 'array')
        G.add_edge('caption', 'code')
        G.add_edge('caption', 'graphic')
        G.add_edge('caption', 'media')
        G.add_edge('caption', 'preformat')
        G.add_edge('caption', 'xref')
        G.add_edge('caption', 'alt-text')
        G.add_edge('caption', 'long-desc')
        G.add_edge('caption', 'email')
        G.add_edge('caption', 'ext-link')
        G.add_edge('caption', 'uri')
        G.add_edge('caption', 'subj-group')
        G.add_edge('caption', 'kwd-group')
        G.add_edge('caption', 'abstract')
        G.add_edge('caption', 'attrib')
        G.add_edge('caption', 'permissions')
        G.add_edge('label', 'accept')
        G.add_edge('label', 'disp-formula')
        G.add_edge('label', 'disp-formula-group')
        G.add_edge('label', 'chem-struct-wrap')
        G.add_edge('label', 'disp-quote')
        G.add_edge('label', 'speech')
        G.add_edge('label', 'statement')
        G.add_edge('label', 'verse-group')
        G.add_edge('label', 'table-wrap')
        G.add_edge('label', 'p')
        G.add_edge('label', 'def-list')
        G.add_edge('label', 'list')
        G.add_edge('label', 'alternatives')
        G.add_edge('label', 'array')
        G.add_edge('label', 'code')
        G.add_edge('label', 'graphic')
        G.add_edge('label', 'media')
        G.add_edge('label', 'preformat')
        G.add_edge('label', 'xref')
        G.add_edge('label', 'alt-text')
        G.add_edge('label', 'long-desc')
        G.add_edge('label', 'email')
        G.add_edge('label', 'ext-link')
        G.add_edge('label', 'uri')
        G.add_edge('label', 'subj-group')
        G.add_edge('label', 'kwd-group')
        G.add_edge('label', 'abstract')
        G.add_edge('label', 'caption')
        G.add_edge('label', 'attrib')
        G.add_edge('label', 'permissions')
        G.add_edge('object-id', 'accept')
        G.add_edge('object-id', 'disp-formula')
        G.add_edge('object-id', 'disp-formula-group')
        G.add_edge('object-id', 'chem-struct-wrap')
        G.add_edge('object-id', 'disp-quote')
        G.add_edge('object-id', 'speech')
        G.add_edge('object-id', 'statement')
        G.add_edge('object-id', 'verse-group')
        G.add_edge('object-id', 'table-wrap')
        G.add_edge('object-id', 'p')
        G.add_edge('object-id', 'def-list')
        G.add_edge('object-id', 'list')
        G.add_edge('object-id', 'alternatives')
        G.add_edge('object-id', 'array')
        G.add_edge('object-id', 'code')
        G.add_edge('object-id', 'graphic')
        G.add_edge('object-id', 'media')
        G.add_edge('object-id', 'preformat')
        G.add_edge('object-id', 'xref')
        G.add_edge('object-id', 'alt-text')
        G.add_edge('object-id', 'long-desc')
        G.add_edge('object-id', 'email')
        G.add_edge('object-id', 'ext-link')
        G.add_edge('object-id', 'uri')
        G.add_edge('object-id', 'subj-group')
        G.add_edge('object-id', 'kwd-group')
        G.add_edge('object-id', 'abstract')
        G.add_edge('object-id', 'caption')
        G.add_edge('object-id', 'label')
        G.add_edge('object-id', 'attrib')
        G.add_edge('object-id', 'permissions')
        G.add_edge('attrib', 'accept')
        G.add_edge('permissions', 'accept')
        return G