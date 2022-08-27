import bibtexparser
import xml.etree.ElementTree as ET

entry_type_dict = {}
entry_type_dict['article'] = 'journal'
entry_type_dict['book'] = 'book'

# does not take care for accents and weird characters
if __name__ == '__main__':
    with open('sample.bib') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

        ref_list = ET.Element('ref-list')

        curr_label = 1
        for entry in bib_database.entries:
            if 'ENTRYTYPE' in entry.keys():
                publication_type = entry_type_dict[entry['ENTRYTYPE'].lower()] 
            else:
                continue 
            ref = ET.SubElement(ref_list, 'ref', attrib={'id': entry['ID']})
            label = ET.SubElement(ref, 'label')
            label.text = str(curr_label)
            curr_label += 1
            element_citation = ET.SubElement(ref, 'element-citation', attrib={'publication-type': publication_type})
            person_group = ET.SubElement(element_citation, 'person-group', attrib={'person-group-type': 'author'})
            authors = entry['author'].split(', ')
            for i in range(len(authors)):
                authors[i] = authors[i].split(' and ')
            for author_list in authors:
                for author in author_list:
                    name = ET.SubElement(person_group, 'name')
                    name_list = author.split(' ')
                    if len(name_list) > 1:
                        surname = ET.SubElement(name, 'surname')
                        surname.text = name_list.pop(-1)
                        given_names = ET.SubElement(name, 'given-names')
                        given_names.text = ' '.join(name_list)
            if 'title' in entry:
                article_title = ET.SubElement(element_citation, 'article-title')
                article_title.text = entry['title']
            if 'volume' in entry:
                volume = ET.SubElement(element_citation, 'volume')
                volume.text = entry['volume']
            if 'pages' in entry:
                pages_list = entry['pages'].split('-')
                fpage = ET.SubElement(element_citation, 'fpage')
                fpage.text = pages_list[0]
                lpage = ET.SubElement(element_citation, 'lpage')
                lpage.text = pages_list[-1]
            if 'year' in entry:
                y = entry['year']
                year = ET.SubElement(element_citation, 'year', attrib={'iso-8601-date': y})
                year.text = y            
            if 'journal' in entry:
                source = ET.SubElement(element_citation, 'source')
                source.text = entry['journal']

            # for key in entry:
            #     print(key + ': ' + entry[key])
            # exit(0)

    tree = ET.ElementTree(ref_list)
    ET.indent(tree, '  ')
    tree.write('references.xml', encoding="utf-8")