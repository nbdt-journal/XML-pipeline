import xml.etree.ElementTree as ET
import xml_parser

def make_conflict_of_interest(root):
    ''' A single COI statement that applies to all contributors but is not explicitly linked to individual contributors in the XML. '''
    data = xml_parser.getSectionData(root, 'sec', 'id', 'conflict-of-interest')
    xml_parser.removeSection(root, 'sec', 'id', 'conflict-of-interest')
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

if __name__ == '__main__':
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    make_conflict_of_interest(root)
    tree.write('sample_output.xml')
