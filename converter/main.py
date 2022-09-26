import os
import json
import subprocess
from converter import endnotes, quotations, src, links, references

def main(input_filepath, output_filepath, reference_input_filepath, reference_output_filepath):
    # fixing end-notes
    endnotes.process_tex.process(input_filepath, 'temp.tex')

    # fixing quotaitons and epigraphs
    
    quotations.process_tex.process('temp.tex', 'temp.tex', quotation_type='quote')
    quotations.process_tex.process('temp.tex', 'temp.tex', quotation_type='epigraph')

    # fixing quotaitons and epigraphs
    quotations.process_tex.process('temp.tex', 'temp.tex', quotation_type='quote')
    quotations.process_tex.process('temp.tex', 'temp.tex', quotation_type='epigraph')

    # fixing end-notes
    endnotes.process_tex.process(input_filepath, 'temp.tex')
    
    # forming the pandoc command 
    command = 'pandoc ' + 'temp.tex' + ' -f latex -t jats -s -o ' + output_filepath
    # the logic is rather simple at the moment
    # python is used to fire a pandoc command with the required inputs
    # os.system(command)
    subprocess.call(command.split(" "))


    with open('quote.json') as json_file:
        quote = json.load(json_file)
    quotations.process_xml.add_quotes(output_filepath, output_filepath, quote)
    with open('epigraph.json') as json_file:
        epigraph = json.load(json_file)
    quotations.process_xml.add_epigraph(output_filepath, output_filepath, epigraph)
    endnotes.process_xml.process(output_filepath, output_filepath)

    
    src.modify.make_conflict_of_interest(output_filepath, output_filepath)

    
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

    # converting references
    
    references.fix_references.process(reference_input_filepath, reference_output_filepath)

    # cleaning-up temporary files
    os.remove('temp.tex')
    os.remove('endnote.json')
    os.remove('epigraph.json')
    os.remove('quote.json')
