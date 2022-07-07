import re 
import json 
from TexSoup import TexSoup

quote_match = [r'\\begin{quote}.*', r'.*\\end{quote}$']
epigraph_match = [r'\\begin{epigraph}.*', r'.*\\end{epigraph}$']

def fix_spacing(content):
    content = re.sub(' +', ' ', content)
    if ord(content[0]) == 32:
        content = content[1:]
    return content

def process(input_filepath, quotation_type='quote'):
    # reading the file 
    f = open(input_filepath, 'r')
    lines = f.readlines()
    f.close()
    # selecting the type
    if quotation_type == 'quote':
        match_sequence = quote_match
    elif quotation_type == 'epigraph':
        match_sequence = epigraph_match
    else:
        print('Invalid Quotation Type!')
        exit(0)
    # initializing the variables
    arr = []
    curr = None 
    line_no = 0 
    line_no_arr = []
    begin_match, end_match = match_sequence 
    # parsing the document
    for line in lines:
        line_no += 1
        if curr is None:
            match = re.findall(begin_match, line)
            if len(match) == 1:
                curr = match[0]
                line_no_arr.append(line_no)
        else:
            curr += line 
            match = re.findall(end_match, line)
            if len(match) == 1:
                soup = TexSoup(curr)
                if quotation_type == 'quote':
                    content = soup.quote 
                elif quotation_type == 'epigraph':
                    content = soup.epigraph 
                arr.append((fix_spacing(content[1]), content[0]))
                curr = None 

    alterTexFile(output_filepath, arr, lines, line_no_arr, quotation_type=quotation_type)

def alterTexFile(output_filepath, arr, lines, line_no_arr, quotation_type='quote'):
    dic = {}
    for i in range(len(line_no_arr)):
        key = quotation_type.upper() + str(i)
        value = arr[i]
        lines.insert(line_no_arr[i]+i-1, key + '\n')
        dic[key] = value
    # deleting the quotations and storing the dictionary
    soup = TexSoup(lines)
    for i in range(len(line_no_arr)):
        if quotation_type == 'quote':
            soup.quote.delete()
            with open("quote.json", "w") as outfile:
                json.dump(dic, outfile)
        elif quotation_type == 'epigraph':
            soup.epigraph.delete()
            with open("epigraph.json", "w") as outfile:
                json.dump(dic, outfile)
        else:
            print('Invalid Quotation Type!')
    # alter the file    
    with open(output_filepath, 'w') as f:
        f.write(str(soup))

if __name__ == '__main__':
    input_filepath='../test.tex'
    output_filepath='out.tex'
    # removing the quotes
    process(input_filepath, quotation_type='quote')
    # removing the epigraphs
    process(output_filepath, quotation_type='epigraph')