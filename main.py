import re 
import dictionaries
import program

lines = []
split_lines = [] 

control = program.Program()

basic_syntax = re.compile("^\s*(\w+):?\s*(\-?\w*)?\s*$")
label_syntax = re.compile("^(\s*(\w)+)\:")
blank_line = re.compile("^\s*$")

with open("teste.txt", "r") as file:
    for line in file:
        line_nocomment = re.sub("\/{2}.*", "", line)

        if blank_line.match(line_nocomment) is None:
            if(basic_syntax.match(line_nocomment)):
                split_line = re.split("\s+", line_nocomment.strip())
                if(label_syntax.match(split_line[0]) is None):
                    lines.append(line_nocomment)
                    split_lines.append(split_line)
                else:
                    control.labels[split_line[0]] = len(lines)
            else:
                print(f'syntax error {line_nocomment}')

control.length = len(lines)

# To-do: Checar se a instrução existe antes de começar a execução. 
# Impedir a execução se houver alguma instrução que não existe.
while control.halt == 0:
    if(split_lines[control.pc][0] in dictionaries.instruction_set):
        print(control.stack)
        print(control.sp)
        print(control.fbr)
        dictionaries.instruction_set[split_lines[control.pc][0]](split_lines[control.pc], control)
        control.pc += 1
    else: 
        print(f'Assembler Error: Unknown instruction "{split_lines[control.pc][0]}".')
        exit(1)

if len(control.stack) != 0:
    print(f'Exit Code: {control.stack[0]}')
else:
    print(f'Exit Code: 0')

if len(control.stack) != 1:
    print(f'Warning: You do not have one item remaining on the stack.') 