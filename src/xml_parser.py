import xml.etree.ElementTree as ET

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

if __name__ == '__main__':
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    removeTag(root, 'sec', 'id', 'conflict-of-interest')
    data = getData(root, 'sec', 'id', 'conflict-of-interest')