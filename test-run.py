import os
import json

# Using pandoc (https://pandoc.org/) to perform a preliminary conversion from LaTeX to JATS-XML.
# The functionality **appears to be** similar to that provided by ALLDocs (https://alldocs.app/convert-latex-to-jats-xml)

if __name__ == '__main__':
    input_filepath = 'main.tex'
    output_filepath = 'main.xml'
    references_filepath = './references/sample.bib'

    # fixing quotaitons and epigraphs
    import quotations
    quotations.process_tex.process('temp.tex', 'temp.tex', quotation_type='quote')
    quotations.process_tex.process('temp.tex', 'temp.tex', quotation_type='epigraph')

    # fixing end-notes
    import endnotes
    endnotes.process_tex.process(input_filepath, 'temp.tex')
    
    # forming the pandoc command 
    command = 'pandoc ' + 'temp.tex' + ' -f latex -t jats -s -o ' + output_filepath
    # the logic is rather simple at the moment
    # python is used to fire a pandoc command with the required inputs
    os.system(command)


    with open('quote.json') as json_file:
        quote = json.load(json_file)
    quotations.process_xml.add_quotes(output_filepath, output_filepath, quote)
    with open('epigraph.json') as json_file:
        epigraph = json.load(json_file)
    quotations.process_xml.add_epigraph(output_filepath, output_filepath, epigraph)
    endnotes.process_xml.process(output_filepath, output_filepath)

    import src
    src.modify.make_conflict_of_interest(output_filepath, output_filepath)

    import links
    links.process_xml.fix_href(output_filepath)
    links.process_xml.fix_xmlns(output_filepath)


    # adding the docstring
    s = '<?xml version="1.0" encoding="utf-8" ?> \n <!DOCTYPE article PUBLIC "-//NLM//DTD JATS (Z39.96) Journal Archiving and Interchange DTD v1.2 20190208//EN" "JATS-archivearticle1.dtd"> \n'
    file_arr = []
    f = open(output_filepath, 'r')
    for line in f:
        file_arr.append(line)
    f.close()
    f = open(output_filepath, 'w')
    f.write(s)
    for line in file_arr:
        f.write(line)
    f.close()