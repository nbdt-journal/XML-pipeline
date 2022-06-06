import os

# Using pandoc (https://pandoc.org/) to perform a preliminary conversion from LaTeX to JATS-XML.
# The functionality **appears to be** similar to that provided by ALLDocs (https://alldocs.app/convert-latex-to-jats-xml)

if __name__ == '__main__':
    input_file_path = 'main.tex' # input file
    output_file_path = 'main.xml' # output file
    
    # forming the pandoc command 
    command = 'pandoc ' + input_file_path + ' -f latex -t jats -s -o ' + output_file_path
    # the logic is rather simple at the moment
    # python is used to fire a pandoc command with the required inputs
    os.system(command)
