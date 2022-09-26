import re
import json
import xml.etree.ElementTree as ET

def process(input_filepath, output_filepath):
    # fix ref marker
    f = open(input_filepath, 'r')
    s = f.read()
    f.close()
    endnote_arr = [each.group(1) for each in re.finditer(r'ENDNOTE\[(.*)\]', s)]
    for each in endnote_arr:
        s = (re.sub('ENDNOTE\[' + each + '\]', '<xref ref-type="sec" rid="e' + each + '"' + '><sup>' + each + '</sup></xref>', s))
    f = open(input_filepath, 'w')
    f.write(s)
    f.close()

    with open('endnote.json', 'r') as f:
        endnotes = json.load(f)

    notes = ET.Element('notes')
    for key in endnotes:
        text = endnotes[key]
        sec = ET.SubElement(notes, 'sec', attrib={'id': 'e' + key[-1]})
        p = ET.SubElement(sec, 'p')
        p.text = text 

    tree = ET.parse(input_filepath)
    root = tree.getroot()
    root[2].insert(1, notes)
    ET.indent(root, '  ')
    tree.write(output_filepath, encoding="utf-8", xml_declaration=True)
    