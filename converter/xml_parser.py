import xml.etree.ElementTree as ET

def make_conflict_of_interest(root):
    ''' A single COI statement that applies to all contributors but is not explicitly linked to individual contributors in the XML. '''
    data = getSectionData(root, 'sec', 'id', 'conflict-of-interest')
    removeSection(root, 'sec', 'id', 'conflict-of-interest')
    author_notes = ET.Element('author-notes')
    fn = ET.SubElement(author_notes, 'fn')
    fn.attrib = {'fn-type': 'COI-statement'}
    for key, text in data:
        if key == 'title':
            continue 
        else:
            paragraph = ET.SubElement(fn, key)
            paragraph.text = text
    store = []
    tag = False
    for child in root:
        if child.tag == 'front':
            for _child in child:
                if _child.tag == 'article-meta':
                    for __child in _child:
                        if __child.tag == 'contrib-group':
                            tag = True
                        elif tag:
                            store.append(__child)
                            _child.remove(__child)
                    _child.append(author_notes)
                    for __child in store:
                        _child.append(__child)

def getSectionData(root, tag, identifier, identifier_name):
    out = []
    for node in root.iter(tag):
        if node.attrib[identifier] == identifier_name.lower():
            for elem in node.iter():
                if elem.tag != node.tag:
                    out.append((elem.tag, elem.text))
    return tuple(out)

def removeSection(root, tag, identifier, identifier_name):
    parent_map = {child: parent for parent in root.iter() for child in parent}
    for node in root.iter(tag):
        if node.attrib[identifier] == identifier_name.lower():
            parent_map[node].remove(node) 