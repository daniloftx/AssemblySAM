#Integer algebra

def add(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 2:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            control.stack.append(control.stack.pop() + control.stack.pop())
            control.sp -= 1
    control.pc += 1

def sub(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 2:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            vt = control.stack.pop()
            vb = control.stack.pop()
            control.stack.append(vb - vt)
            control.sp -= 1
    control.pc += 1
        
def times(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 2:
            print(f'{line[0]} error')
            control.halt = 1
        else:
          control.stack.append(control.stack.pop() * control.stack.pop())
          control.sp -= 1
    control.pc += 1

def div(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 2:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            vt = control.stack.pop()
            vb = control.stack.pop()
            control.stack.append(vb // vt)
            control.sp -= 1
    control.pc += 1
    
def mod(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 2:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            vt = control.stack.pop()
            vb = control.stack.pop()
            control.stack.append(vb % vt)
            control.sp -= 1
    control.pc += 1

#Comparison
def cmp(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 2:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            vt = control.stack.pop()
            vb = control.stack.pop()
            if vt > vb:
                control.stack.append(1)
            elif vt == vb:
                control.stack.append(0)
            else:
                control.stack.append(-1)
            control.sp -= 1
    control.pc += 1
            

def greater(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 2:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            vt = control.stack.pop()
            vb = control.stack.pop()
            if vt < vb:
                control.stack.append(1)
            else:
                control.stack.append(0)
            control.sp -= 1
    control.pc += 1

def less(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 2:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            vt = control.stack.pop()
            vb = control.stack.pop()
            if vt > vb:
                control.stack.append(1)
            else:
                control.stack.append(0)
            control.sp -= 1
    control.pc += 1

def equal(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 2:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            vt = control.stack.pop()
            vb = control.stack.pop()
            if vt == vb:
                control.stack.append(1)
            else:
                control.stack.append(0)
            control.sp -= 1
    control.pc += 1

def isnil(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 1:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            if control.stack.pop() == 0:
                control.stack.append(1)
            else:
                control.stack.append(0)
    control.pc += 1
            
def ispos(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 1:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            if control.stack.pop() > 0:
                control.stack.append(1)
            else:
                control.stack.append(0)
    control.pc += 1

def isneg(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if len(control.stack) < 1:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            if control.stack.pop() < 0:
                control.stack.append(1)
            else:
                control.stack.append(0)
    control.pc += 1

#jumps
def jump(line, control):
    if len(line) < 2:
        print(f'{line[0]} error')
    else:
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                print(f'{line[0]} error')
                control.halt = 1
            else:
                control.pc = int(n)
        else:
            if n+':' in control.labels:
                control.pc = control.labels[n+':']
            else: 
                print(f'Adress {n} not found')

def jumpc(line, control):
    if len(line) < 2:
        print(f'{line[0]} error')
    else:
        if(control.stack[control.sp - 1] != 0):
            n = line[1].lstrip('-')
            if n.isdigit():
                if line[1][0] == '-':
                    print(f'{line[0]} error')
                    control.halt = 1
                else:              
                    control.pc = int(n)
            else:
                if n+':' in control.labels:     
                    control.pc = control.labels[n+':']
                else: 
                    print(f'Adress {n} not found')

def jsr(line, control):
    if len(line) < 2:
        print(f'{line[0]} error')
    else:
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                print(f'{line[0]} error')
                control.halt = 1
            else:
                control.stack.append(control.pc + 1)
                control.pc = int(n)
        else:
            if n+':' in control.labels:
                control.stack.append(control.pc + 1)
                control.pc = control.labels[n+':']
            else: 
                print(f'Adress {n} not found')
        control.sp += 1

def skip(line, control):
    print("skip func")

#stack frames
def link(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        control.stack.append(control.fbr)
        control.fbr = control.sp
        control.sp += 1
    control.pc += 1

def unlink(line, control):
    popfbr(line, control)
    control.pc += 1

#stop
def stop(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
    control.halt = 1
        

#absolute store
def pushabs(line, control):
    if len(line) < 2:
        print(f'{line[0]} error')
        control.halt = 1
    else: 
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                print(f'{line[0]} error')
                control.halt = 1
            else:
                control.stack.append(control.stack[ int(n)])
            control.sp += 1
        else:
            print(f'{line[0]} error')
            control.halt = 1
    control.pc += 1

def storeabs(line, control):
    if len(line) < 2:
        print(f'{line[0]} error')
        control.halt = 1
    else: 
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                print(f'{line[0]} error')
                control.halt = 1
            else:   
                while int(n) >= len(control.stack):
                    control.stack.append(0)
                    control.sp += 1
                control.stack[int(n)] = control.stack[len(control.stack) - 1]
        else:
            print(f'{line[0]} error')
            control.halt = 1
    control.pc += 1
    
#relative store
def pushoff(line, control):
    if len(line) < 2:
        print(f'{line[0]} error')
        control.halt = 1
    else: 
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                v = control.fbr - int(n)
                if v < 0:
                    print(f'{line[0]} error')
                    control.halt = 1
                else:   
                    control.stack.append(control.stack[v])
            else:
                control.stack.append(control.stack[control.fbr + int(n)])
            control.sp += 1
        else:
            print(f'{line[0]} error')
            control.halt = 1
    control.pc += 1

def storeoff(line, control):
    if len(line) < 2:
        print(f'{line[0]} error1')
        control.halt = 1
    else: 
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                v = control.fbr - int(n)
                if v < 0:
                    print(f'{control.fbr} {line[1]}')
                    print(f'{line[0]} error2')
                    control.halt = 1
                else:   
                    control.stack[v] = control.stack.pop()
            else:
                control.stack[control.fbr + int(n)] = control.stack.pop()
            control.sp -= 1
        else:
            print(f'{line[0]} error3')
            control.halt = 1
    control.pc += 1

def popfbr(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        if control.sp - 1 < 0:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            control.fbr = control.stack[control.sp-1]
    control.pc += 1

def pushfbr(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        control.stack.append(control.fbr)
        control.sp += 1
    control.pc += 1
    
#insertion
def pushimm(line, control):
    n = line[1].lstrip('-')
    if n.isdigit():
        if line[1][0] == '-':
            control.stack.append(int(n) * -1)
        else:
            control.stack.append(int(n))
    else:
        print(f'{line[0]} error')
        control.halt = 1
    control.pc += 1

#addsp
def addsp(line, control):
    if len(line) < 2:
        print(f'{line[0]} error')
        control.halt = 1
    else: 
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                control.sp -= int(n)
            else:
                control.sp += int(n)
            if control.sp < 0:
                print(f'{line[0]} error')
                control.halt = 1
        else:
            print(f'{line[0]} error')
            control.halt = 1
    control.pc += 1


def pushsp(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        control.stack.append(control.sp)
        control.sp += 1
    control.pc += 1

def popsp(line, control):
    if len(line) > 1:
        print(f'{line[0]} error')
        control.halt = 1
    else:
        control.sp -= 1
        if control.sp < 0:
            print(f'{line[0]} error')
            control.halt = 1
        else:
            control.sp = control.stack[control.sp]
    control.pc += 1