import re 
import dictionaries
import labels

lines = []

basic_syntax = re.compile("^\s*(\w+):?\s*(\-?\w*)?($|\s*//)")
label_syntax = re.compile("^(\s*(\w)+)\:")
blank_line = re.compile("^\s*$")
split_lines = [] 

file = open("teste.txt", "r")

for line in file:
    line_nocomment = re.sub("\/{2}.*", "", line)
    if blank_line.match(line_nocomment) is None:
        if(basic_syntax.match(line_nocomment)):
            split_line = re.split("\s+", line_nocomment.strip())
            if(label_syntax.match(split_line[0]) is None):
                lines.append(line_nocomment)
                split_lines.append(split_line)
            else:
                labels.labels[split_line[0]] = len(lines)
        else:
            print("syntax error")

for current_line, line in enumerate(lines):
    if(split_lines[current_line][0] in dictionaries.instruction_set):
        dictionaries.instruction_set[split_lines[current_line][0]](split_lines[current_line], [])
    else: 
        print("instruction not found ")