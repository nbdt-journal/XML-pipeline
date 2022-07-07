import json 
import xml.etree.ElementTree as ET

def add_quotes(input_filepath, dic):
    tree = ET.parse(input_filepath)
    root = tree.getroot()
    parent_map = {c:p for p in root.iter() for c in p}
    remove = []
    for child in root.iter():
        if child.tag == 'p':
            if 'QUOTE' in child.text: 
                print(child.text)
                text, attribute = dic[child.text]
                disp_quote = ET.Element('disp-quote')
                p = ET.SubElement(disp_quote, 'p')
                p.text = text 
                attrib = ET.SubElement(disp_quote, 'attrib')
                attrib.text = attribute    
                parent = parent_map[child]
                index = list(parent).index(child)
                parent.remove(child)
                parent.insert(index, disp_quote)
    ET.indent(root, '  ')
    tree.write('out.xml', encoding="utf-8", xml_declaration=True)


if __name__ == '__main__':
    with open('quote.json', 'r') as f:
        quotes = json.load(f)
    with open('epigraph.json', 'r') as f:
        epigraphs = json.load(f)

    add_quotes('sample.xml', quotes)