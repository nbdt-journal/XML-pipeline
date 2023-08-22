import networkx as nx

class Sup:
    def __init__(self):
        self.name = 'sup' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('#PCDATA')
        G.add_node('email')
        G.add_node('ext-link')
        G.add_node('uri')
        G.add_node('inline-supplementary-material')
        G.add_node('related-article')
        G.add_node('related-object')
        G.add_node('hr')
        G.add_node('bold')
        G.add_node('fixed-case')
        G.add_node('italic')
        G.add_node('monospace')
        G.add_node('overline')
        G.add_node('overline-start')
        G.add_node('overline-end')
        G.add_node('roman')
        G.add_node('sans-serif')
        G.add_node('sc')
        G.add_node('strike')
        G.add_node('underline')
        G.add_node('underline-start')
        G.add_node('underline-end')
        G.add_node('ruby')
        G.add_node('alternatives')
        G.add_node('inline-graphic')
        G.add_node('inline-media')
        G.add_node('private-char')
        G.add_node('chem-struct')
        G.add_node('inline-formula')
        G.add_node('tex-math')
        G.add_node('mml:math')
        G.add_node('abbrev')
        G.add_node('index-term')
        G.add_node('index-term-range-end')
        G.add_node('milestone-end')
        G.add_node('milestone-start')
        G.add_node('named-content')
        G.add_node('styled-content')
        G.add_node('fn')
        G.add_node('target')
        G.add_node('xref')
        G.add_node('sub')
        G.add_node('sup')
        G.add_node('x')
        G.add_node('break')
        #adding edges
        G.add_edge('start', '#PCDATA')
        G.add_edge('start', 'email')
        G.add_edge('start', 'ext-link')
        G.add_edge('start', 'uri')
        G.add_edge('start', 'inline-supplementary-material')
        G.add_edge('start', 'related-article')
        G.add_edge('start', 'related-object')
        G.add_edge('start', 'hr')
        G.add_edge('start', 'bold')
        G.add_edge('start', 'fixed-case')
        G.add_edge('start', 'italic')
        G.add_edge('start', 'monospace')
        G.add_edge('start', 'overline')
        G.add_edge('start', 'overline-start')
        G.add_edge('start', 'overline-end')
        G.add_edge('start', 'roman')
        G.add_edge('start', 'sans-serif')
        G.add_edge('start', 'sc')
        G.add_edge('start', 'strike')
        G.add_edge('start', 'underline')
        G.add_edge('start', 'underline-start')
        G.add_edge('start', 'underline-end')
        G.add_edge('start', 'ruby')
        G.add_edge('start', 'alternatives')
        G.add_edge('start', 'inline-graphic')
        G.add_edge('start', 'inline-media')
        G.add_edge('start', 'private-char')
        G.add_edge('start', 'chem-struct')
        G.add_edge('start', 'inline-formula')
        G.add_edge('start', 'tex-math')
        G.add_edge('start', 'mml:math')
        G.add_edge('start', 'abbrev')
        G.add_edge('start', 'index-term')
        G.add_edge('start', 'index-term-range-end')
        G.add_edge('start', 'milestone-end')
        G.add_edge('start', 'milestone-start')
        G.add_edge('start', 'named-content')
        G.add_edge('start', 'styled-content')
        G.add_edge('start', 'fn')
        G.add_edge('start', 'target')
        G.add_edge('start', 'xref')
        G.add_edge('start', 'sub')
        G.add_edge('start', 'sup')
        G.add_edge('start', 'x')
        G.add_edge('start', 'break')
        G.add_edge('start', 'accept')
        G.add_edge('#PCDATA', 'accept')
        G.add_edge('email', 'accept')
        G.add_edge('ext-link', 'accept')
        G.add_edge('uri', 'accept')
        G.add_edge('inline-supplementary-material', 'accept')
        G.add_edge('related-article', 'accept')
        G.add_edge('related-object', 'accept')
        G.add_edge('hr', 'accept')
        G.add_edge('bold', 'accept')
        G.add_edge('fixed-case', 'accept')
        G.add_edge('italic', 'accept')
        G.add_edge('monospace', 'accept')
        G.add_edge('overline', 'accept')
        G.add_edge('overline-start', 'accept')
        G.add_edge('overline-end', 'accept')
        G.add_edge('roman', 'accept')
        G.add_edge('sans-serif', 'accept')
        G.add_edge('sc', 'accept')
        G.add_edge('strike', 'accept')
        G.add_edge('underline', 'accept')
        G.add_edge('underline-start', 'accept')
        G.add_edge('underline-end', 'accept')
        G.add_edge('ruby', 'accept')
        G.add_edge('alternatives', 'accept')
        G.add_edge('inline-graphic', 'accept')
        G.add_edge('inline-media', 'accept')
        G.add_edge('private-char', 'accept')
        G.add_edge('chem-struct', 'accept')
        G.add_edge('inline-formula', 'accept')
        G.add_edge('tex-math', 'accept')
        G.add_edge('mml:math', 'accept')
        G.add_edge('abbrev', 'accept')
        G.add_edge('index-term', 'accept')
        G.add_edge('index-term-range-end', 'accept')
        G.add_edge('milestone-end', 'accept')
        G.add_edge('milestone-start', 'accept')
        G.add_edge('named-content', 'accept')
        G.add_edge('styled-content', 'accept')
        G.add_edge('fn', 'accept')
        G.add_edge('target', 'accept')
        G.add_edge('xref', 'accept')
        G.add_edge('sub', 'accept')
        G.add_edge('sup', 'accept')
        G.add_edge('x', 'accept')
        G.add_edge('break', 'accept')
        return G