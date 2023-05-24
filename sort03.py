import re 

file = open('workfile01.txt', 'r')

text = file.read()

file.close()

lines = text.split('\n')

for i in range(len(lines)):
    words = lines[i].split()
    for j in range(len(words)):
        if words[j] == '1701D0Ff039Fyy19vv11vd':
            words[j] = '<a href="https://github.com/gustav4/s?='
        elif words[j] == 'tt67y2AH1719tt':
            words[j] = '">' 
        elif words[j] == '200667h235395719JL19a07f54ty': 
            words[j] = '</a><br>'  
        elif words[j] == 'dd44dd': 
            words[j] = "br d4"
    new_line = ' '.join(words)
    new_line = new_line.rstrip()
    lines[i] = new_line
text = '\n'.join(lines)
file = open('outworkfile03.html', 'w')
file.write(text)
file.close()
