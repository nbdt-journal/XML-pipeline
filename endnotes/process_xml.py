import re
import json
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    # fix ref marker
    f = open('out.xml', 'r')
    s = f.read()
    f.close()
    endnote_arr = [each.group(1) for each in re.finditer(r'ENDNOTE\[(.*)\]', s)]
    for each in endnote_arr:
        s = (re.sub('ENDNOTE\[' + each + '\]', '<ref id="endnotes' + each + '"><sup>' + each + '</sup></ref>', s))
    f = open('out.xml', 'w')
    f.write(s)
    f.close()

    with open('endnote.json', 'r') as f:
        endnotes = json.load(f)

    notes = ET.Element('notes')
    for key in endnotes:
        text = endnotes[key]
        sec = ET.SubElement(notes, 'sec', attrib={'id': 'endnotes' + key[-1]})
        sec.text = text 

    tree = ET.parse('out.xml')
    root = tree.getroot()
    root[2].insert(1, notes)
    ET.indent(root, '  ')
    tree.write('dummy.xml', encoding="utf-8", xml_declaration=True)
    