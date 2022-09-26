# XML-pipeline

The pipeline aims to convert NBDT (Neurons, Behavior, Data analysis, and Theory) Journal submissions, in LaTeX, to Journal Publishing Tag Library NISO JATS Version 1.3 (ANSI/NISO Z39.96-2021). 

The application builds on top of Pandoc, which is a universal document converter. Where pandoc does convert LaTeX documents to XML, there are several shortcomings to the existing functionality. The conversion does not account for all the macros used by NBDT. Moreover, the converted documents do not comply with the required JATS Version 1.3. 

XML-Pipeline uses pandoc and contains a set of python scripts to convert NDBT submissions into XML files that validate through JATS Version 1.3.

## Available Functionality

Currently, the application takes separate inputs for the references and the remaining manuscript. The pipeline runs through `main.py`.
* `reference_input_filepath`: path of the '.bib' file. 
* 'reference_output_filepath`: the path of the '.xml' file with the converted bibliography.
* `input_filepath`: the path of the '.tex' file (remainder of the manuscript).
* `output_filepath`: the path of the '.xml' file with the converted manuscript.

Both the output '.xml' files comply with the JATS Version 1.3. Hence, the application takes two separate files as input, and then returns their XML conversions.

## Requirements
### Installing Python Libraries

pip install re
pip install json
pip install texsoup
pip install elementpath
pip install bibtexparser

## Test
The following files:
* `main.tex`
* `sample.bib`

are used to test the application. Running `main.py` converts both the manuscript file (`main.tex`) and bibliography file (`sample.bib`) into XML files with the corresponding names (and '.xml' extension).