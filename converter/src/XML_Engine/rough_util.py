import re
s = '(address | alternatives | answer | answer-set | array | block-alternatives | boxed-text | chem-struct-wrap | code | explanation | fig | fig-group | graphic | media | preformat | question | question-wrap | question-wrap-group | supplementary-material | table-wrap | table-wrap-group | disp-formula | disp-formula-group | def-list | list | tex-math | mml:math | p | related-article | related-object | disp-quote | speech | statement | verse-group)*'

l = s.split(' | ')

for i in range(len(l)):
    l[i] = l[i].replace('-', '_')
    l[i] = l[i].replace(':', '_')
    
l[-1] = re.sub('\W+','', l[-1])
arr = ['node.get_first_node()', 'node.get_last_node()']
for each in l:
    if '#' in each:
        continue 
    if each[0] == '(':
        each = each[1:]
    if 'mmlmath' in each:
        each = 'mml_math'
    arr.append(each + '_node')
    
tag = 0
for each in arr:
    if tag == 0:
        print('[', end='')
        tag = 1
    if each != arr[-1]:
        print(each + ', ', end='')
    else:
        print(each, end='')
print(']')

