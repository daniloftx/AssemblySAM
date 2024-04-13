import re 
import dictionaries
import labels

lines = []

basic_syntax = re.compile("^((\s)*\/{2})|^\s*(\w)+\:?\s*((\-?\w)*)?($|(\s*\/{2}))")
comment_syntax = re.compile("^(\/{2})")
label_syntax = re.compile("^(\s*(\w)+)\:")
blank_line = re.compile("^\s*$")
split_lines = [] 
#print(hBox.match(s))
#print(re.split("\s+", s.strip()))

#for i in re.split("\s+", s.strip()):
#    print(i)
file = open("teste.txt", "r")

for line in file:
    if blank_line.match(line) is None:
        if(basic_syntax.match(line)):
            split_line = re.split("\s+", line.strip())
            #print(split_line)
            if(comment_syntax.match(split_line[0]) is None):
                if(label_syntax.match(split_line[0]) is None):
                    lines.append(line)
                    split_lines.append(split_line)
                    #print(line)
                else:
                    labels.labels[split_line[0]] = len(lines)
        else:
            print("syntax error")

for current_line, line in enumerate(lines):
    if(split_lines[current_line][0] in dictionaries.instruction_set):
        dictionaries.instruction_set[split_lines[current_line][0]](split_lines[current_line], [])
    else:
        print("instruction not found")