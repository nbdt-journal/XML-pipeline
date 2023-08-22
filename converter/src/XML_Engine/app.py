import networkx as nx

class App:
    def __init__(self):
        self.name = 'app' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('permissions')
        G.add_node('sec-meta')
        G.add_node('label')
        G.add_node('title')
        G.add_node('sec')
        G.add_node('address')
        G.add_node('alternatives')
        G.add_node('answer')
        G.add_node('answer-set')
        G.add_node('array')
        G.add_node('block-alternatives')
        G.add_node('boxed-text')
        G.add_node('chem-struct-wrap')
        G.add_node('code')
        G.add_node('explanation')
        G.add_node('fig')
        G.add_node('fig-group')
        G.add_node('graphic')
        G.add_node('media')
        G.add_node('preformat')
        G.add_node('question')
        G.add_node('question-wrap')
        G.add_node('question-wrap-group')
        G.add_node('supplementary-material')
        G.add_node('table-wrap')
        G.add_node('table-wrap-group')
        G.add_node('disp-formula')
        G.add_node('disp-formula-group')
        G.add_node('def-list')
        G.add_node('list')
        G.add_node('tex-math')
        G.add_node('mml:math')
        G.add_node('p')
        G.add_node('related-article')
        G.add_node('related-object')
        G.add_node('ack')
        G.add_node('disp-quote')
        G.add_node('speech')
        G.add_node('statement')
        G.add_node('verse-group')
        G.add_node('x')
        G.add_node('notes')
        G.add_node('fn-group')
        G.add_node('glossary')
        G.add_node('ref-list')
        #adding edges
        G.add_edge('start', 'sec-meta')
        G.add_edge('start', 'permissions')
        G.add_edge('start', 'accept')
        G.add_edge('sec-meta', 'permissions')
        G.add_edge('sec-meta', 'accept')
        G.add_edge('label', 'permissions')
        G.add_edge('label', 'accept')
        G.add_edge('title', 'permissions')
        G.add_edge('title', 'accept')
        G.add_edge('sec', 'permissions')
        G.add_edge('sec', 'accept')
        G.add_edge('address', 'permissions')
        G.add_edge('address', 'accept')
        G.add_edge('alternatives', 'permissions')
        G.add_edge('alternatives', 'accept')
        G.add_edge('answer', 'permissions')
        G.add_edge('answer', 'accept')
        G.add_edge('answer-set', 'permissions')
        G.add_edge('answer-set', 'accept')
        G.add_edge('array', 'permissions')
        G.add_edge('array', 'accept')
        G.add_edge('block-alternatives', 'permissions')
        G.add_edge('block-alternatives', 'accept')
        G.add_edge('boxed-text', 'permissions')
        G.add_edge('boxed-text', 'accept')
        G.add_edge('chem-struct-wrap', 'permissions')
        G.add_edge('chem-struct-wrap', 'accept')
        G.add_edge('code', 'permissions')
        G.add_edge('code', 'accept')
        G.add_edge('explanation', 'permissions')
        G.add_edge('explanation', 'accept')
        G.add_edge('fig', 'permissions')
        G.add_edge('fig', 'accept')
        G.add_edge('fig-group', 'permissions')
        G.add_edge('fig-group', 'accept')
        G.add_edge('graphic', 'permissions')
        G.add_edge('graphic', 'accept')
        G.add_edge('media', 'permissions')
        G.add_edge('media', 'accept')
        G.add_edge('preformat', 'permissions')
        G.add_edge('preformat', 'accept')
        G.add_edge('question', 'permissions')
        G.add_edge('question', 'accept')
        G.add_edge('question-wrap', 'permissions')
        G.add_edge('question-wrap', 'accept')
        G.add_edge('question-wrap-group', 'permissions')
        G.add_edge('question-wrap-group', 'accept')
        G.add_edge('supplementary-material', 'permissions')
        G.add_edge('supplementary-material', 'accept')
        G.add_edge('table-wrap', 'permissions')
        G.add_edge('table-wrap', 'accept')
        G.add_edge('table-wrap-group', 'permissions')
        G.add_edge('table-wrap-group', 'accept')
        G.add_edge('disp-formula', 'permissions')
        G.add_edge('disp-formula', 'accept')
        G.add_edge('disp-formula-group', 'permissions')
        G.add_edge('disp-formula-group', 'accept')
        G.add_edge('def-list', 'permissions')
        G.add_edge('def-list', 'accept')
        G.add_edge('list', 'permissions')
        G.add_edge('list', 'accept')
        G.add_edge('tex-math', 'permissions')
        G.add_edge('tex-math', 'accept')
        G.add_edge('mml:math', 'permissions')
        G.add_edge('mml:math', 'accept')
        G.add_edge('p', 'permissions')
        G.add_edge('p', 'accept')
        G.add_edge('related-article', 'permissions')
        G.add_edge('related-article', 'accept')
        G.add_edge('related-object', 'permissions')
        G.add_edge('related-object', 'accept')
        G.add_edge('ack', 'permissions')
        G.add_edge('ack', 'accept')
        G.add_edge('disp-quote', 'permissions')
        G.add_edge('disp-quote', 'accept')
        G.add_edge('speech', 'permissions')
        G.add_edge('speech', 'accept')
        G.add_edge('statement', 'permissions')
        G.add_edge('statement', 'accept')
        G.add_edge('verse-group', 'permissions')
        G.add_edge('verse-group', 'accept')
        G.add_edge('x', 'permissions')
        G.add_edge('x', 'accept')
        G.add_edge('notes', 'permissions')
        G.add_edge('notes', 'accept')
        G.add_edge('fn-group', 'permissions')
        G.add_edge('fn-group', 'accept')
        G.add_edge('glossary', 'permissions')
        G.add_edge('glossary', 'accept')
        G.add_edge('ref-list', 'permissions')
        G.add_edge('ref-list', 'accept')
        return G