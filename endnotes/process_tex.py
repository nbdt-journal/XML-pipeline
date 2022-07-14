import re 
import json 

endnote_match = r'\\endnote{(.*)}'

f = open('../main.tex', 'r')
s = f.read()
f.close()

dic = {}

endnotes = [each.group(1) for each in re.finditer(endnote_match, s)]
for i in range(len(endnotes)):
    dic['ENDNOTE' + str(i)] = endnotes[i]

with open("endnote.json", "w") as outfile:
    json.dump(dic, outfile)

s = re.sub(endnote_match, 'ENDNOTE', s)

s = s.split('ENDNOTE')
for i in range(len(s)-1):
    s[i] += 'ENDNOTE[' + str(i) + ']'
s = ''.join(s)

f = open('out.tex', 'w')
f.write(s)
f.close()