import xml.etree.ElementTree as ET
from . import xml_parser

def make_conflict_of_interest(input_filename, output_filename):
    tree = ET.parse(input_filename)
    root = tree.getroot()
    ''' A single COI statement that applies to all contributors but is not explicitly linked to individual contributors in the XML. '''
    data = xml_parser.getSectionData(root, 'sec', 'id', 'conflict-of-interest')
    temp = []
    for each in data:
        if each[0] == 'boxed-text':
            continue
        temp.append(each)
    data = tuple(temp)
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
    tree.write(output_filename)

if __name__ == '__main__':
    input_filename = 'sample.xml'
    output_filename = 'sample_output.xml'
    make_conflict_of_interest(input_filename, output_filename)