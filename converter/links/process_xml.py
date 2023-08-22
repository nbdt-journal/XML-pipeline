import re

types_of_links = ['actuate', 'href', 'role', 'show', 'title', 'type', 'xlink', 'base', 'lang', 'mathml']

mml_tags = ['maction', 'math', 'menclose', 'merror', 'mfenced', 'mfrac', 'mi', 'mmultiscripts', 'mn', 'mo', 'mover', 'mpadded', 'mphantom', 'mroot', 'mrow', 'ms', 'mspace', 'msqrt', 'mstyle', 'msub', 'msubsup', 'msup', 'mtable', 'mtd', 'mtext', 'mtr', 'munder', 'munderover', 'semantics']

def find_type_of_link(s):
    for each in types_of_links:
        if len(s) >= len(each):
            if s[-len(each)-1:-1].lower() == each:
                return each 

def fix_xmlns(filename):
    new_file = []
    with open(filename) as file:
        for line in file:
            if 'xmlns:' in line:
                temp = line.split()
                for i in range(len(temp)):
                    if 'xmlns:' in temp[i]:
                        to_replace = re.findall(r'xmlns:(.*?)=', temp[i])[0]
                        replace_with = find_type_of_link(temp[i])
                        if replace_with != 'mathml':
                            temp[i] = temp[i].replace(to_replace, replace_with)
                        else:
                            temp[i] = temp[i].replace(to_replace, 'mml')
                        line = ' '.join(temp)

            for each in mml_tags:
                tag = 0
                if each in line:
                    try:
                        index = line.index(':' + each)
                        tag = 1
                    except:
                        pass
                    if tag == 1:
                        line = line.replace(line[index-3:index], 'mml')
            new_file.append(line)
    
    f = open(filename, 'w')
    for line in new_file:
        f.write(line)
    f.close()
 
def fix_href(filename):
    new_file = []
    with open(filename) as file:
        for line in file:
            if 'ns0:href' in line:
                line = line.replace('ns0:href', 'xlink:href')
                line = line.replace('ns0', 'xlink')
            new_file.append(line) 

    f = open(filename, 'w')
    for line in new_file:
        f.write(line)
    f.close()

if __name__ == '__main__':
    filename = '../main.xml'
    fix_href(filename)
    fix_xmlns(filename)