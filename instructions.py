#Integer algebra

def add(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        control.stack.append(control.pop() + control.pop())
        control.sp -= 1

def addf(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        control.stack.append(control.pop() + control.pop())
        control.sp -= 1

def sub(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        vb = control.pop()

        control.stack.append(vb - vt)

        control.sp -= 1

def subf(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        vb = control.pop()

        control.stack.append(vb - vt)

        control.sp -= 1

def times(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        control.stack.append(control.pop() * control.pop())

        control.sp -= 1

def timesf(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        control.stack.append(control.pop() * control.pop())

        control.sp -= 1

def div(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        vb = control.pop()

        control.stack.append(vb // vt)

        control.sp -= 1

def divf(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        vb = control.pop()

        control.stack.append(vb / vt)

        control.sp -= 1

def mod(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        vb = control.pop()

        control.stack.append(vb % vt)

        control.sp -= 1

#Comparison
def cmp(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        vb = control.pop()

        if vt > vb:
            control.stack.append(1)
        elif vt == vb:
            control.stack.append(0)
        else:
            control.stack.append(-1)

        control.sp -= 1

def greater(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        vb = control.pop()

        if vb > vt:
            control.stack.append(1)
        else:
            control.stack.append(0)

        control.sp -= 1

def less(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        vb = control.pop()

        if vb < vt:
            control.stack.append(1)
        else:
            control.stack.append(0)

        control.sp -= 1

def equal(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        vb = control.pop()

        if vt == vb:
            control.stack.append(1)
        else:
            control.stack.append(0)

        control.sp -= 1

def isnil(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        if control.pop() == 0:
            control.stack.append(1)
        else:
            control.stack.append(0)

def ispos(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        if control.pop() > 0:
            control.stack.append(1)
        else:
            control.stack.append(0)

def isneg(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        if control.pop() < 0:
            control.stack.append(1)
        else:
            control.stack.append(0)

#jumps
def jump(line, control):
    if len(line) < 2:
        print(f'Error in instruction "{line[0]}" too few arguments.')
        control.halt = 1
        control.error = True
    else:
        n = line[1].lstrip('-')
        if n.isdigit():
            if int(n) > control.length - 1:
                print(f'Processor Error: Invalid index at instruction {control.pc}.')
                control.error = True
                exit(1)

            if line[1][0] == '-':
                print(f'Error in instruction "{line[0]}" not expecting negative number.')
                control.error = True
                control.halt = 1
            else:
                # Subtract 1 because pc will be incremented after this function execution
                control.pc = int(n) - 1
        else:
            if n+':' in control.labels:
                # Subtract 1 for same reason above
                control.pc = control.labels[n+':'] - 1
            else: 
                print(f'Processor Error: Unresolved reference "{n}" at instruction {control.pc}.')
                control.error = True
                exit(1)

def jumpc(line, control):
    if len(line) < 2:
        print(f'Error in instruction "{line[0]}" too few arguments.')
        control.halt = 1
        control.error = True
    else:
        vt = control.pop()
        control.sp -= 1
        if(vt != 0):
            n = line[1].lstrip('-')

            if n.isdigit():
                if line[1][0] == '-':
                    print(f'Error in instruction "{line[0]}" not expecting negative number.')
                    control.halt = 1
                    control.error = True
                else:              
                    # Subtract 1 because pc will be incremented after this function execution
                    control.pc = int(n) - 1
            else:
                if n+':' in control.labels:     
                    # Subtract 1 for same reason above
                    control.pc = control.labels[n+':'] - 1
                else: 
                    print(f'Processor Error: Unresolved reference "{n}" at instruction {control.pc}.')
                    control.error = True
                    exit(1)

def jsr(line, control):
    if len(line) < 2:
        print(f'Error in instruction "{line[0]}" too few arguments.')
        control.halt = 1
        control.error = True
    else:
        n = line[1].lstrip('-')

        if n.isdigit():
            if line[1][0] == '-':
                print(f'Error in instruction "{line[0]}" not expecting negative number.')
                control.error = True
                control.halt = 1
            else:
                control.stack.append(control.pc + 1)

                # Subtract 1 because pc will be incremented after this function execution
                control.pc = int(n) - 1
        else:
            if n+':' in control.labels:
                control.stack.append(control.pc + 1)

                # Subtract 1 for same reason above
                control.pc = control.labels[n+':'] - 1
            else: 
                print(f'Processor Error: Unresolved reference "{n}" at instruction {control.pc}.')
                control.error = True
                exit(1)

        control.sp += 1

def jumpind(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        control.sp -= 1
        vt = control.pop()
        if vt < 0:
            print(f'Invalid PC {control.pc} address')
            control.error = True
            control.halt = 1
        else:
            control.pc = vt - 1

#stack frames
def link(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        control.stack.append(control.fbr)
        control.fbr = control.sp
        control.sp += 1

def unlink(line, control):
    popfbr(line, control)

#stop
def stop(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.error = True
    control.halt = 1


#absolute store
def pushabs(line, control):
    if len(line) < 2:
        print(f'Error in instruction "{line[0]}" too few arguments.')
        control.halt = 1
        control.error = True
        
    else: 
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                print(f'Error in instruction "{line[0]}" not expecting negative number.')
                control.halt = 1
                control.error = True
            else:
                control.stack.append(control.stack[ int(n)])
            control.sp += 1
        else:
            print(f'Error in instruction "{line[0]}" expecting a number')
            control.halt = 1
            control.error = True

def storeabs(line, control):
    if len(line) < 2:
        print(f'Error in instruction "{line[0]}" too few arguments.')
        control.halt = 1
        control.error = True
        
    else: 
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                print(f'Error in instruction "{line[0]}" not expecting negative number.')
                control.halt = 1
                control.error = True
            else:
                control.stack[ int(n)] = control.pop()
            control.sp -= 1
        else:
            print(f'Error in instruction "{line[0]}" expecting a number')
            control.halt = 1
            control.error = True

#relative store
def pushoff(line, control):
    if len(line) < 2:
        print(f'Error in instruction "{line[0]}" too few arguments.')
        control.halt = 1
        control.error = True
        
    else: 
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                v = control.fbr - int(n)
                if v < 0:
                    print(f'Error in instruction "{line[0]}" FBR cannot be negative.')
                    control.halt = 1
                    control.error = True
                else:   
                    control.stack.append(control.stack[v])
            else:
                control.stack.append(control.stack[control.fbr + int(n)])
            control.sp += 1
        else:
            print(f'Error in instruction "{line[0]}" expecting a number')
            control.halt = 1
            control.error = True

def storeoff(line, control):
    if len(line) < 2:
        print(f'Error in instruction "{line[0]}" too few arguments.')
        control.halt = 1
        control.error = True
        
    else: 
        n = line[1].lstrip('-')
        if n.isdigit():
            if line[1][0] == '-':
                v = control.fbr - int(n)
                if v < 0:
                    print(f'Error in instruction "{line[0]}" FBR cannot be negative.')
                    control.halt = 1
                    control.error = True
                else:   
                    control.stack[v] = control.pop()
            else:
                control.stack[control.fbr + int(n)] = control.pop()
            control.sp -= 1
        else:
            print(f'Error in instruction "{line[0]}" expecting a number')
            control.halt = 1
            control.error = True

def popfbr(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        if control.sp - 1 < 0:
            print(f'Error in instruction "{line[0]}" SP cannot be negative.')
            control.halt = 1
            control.error = True
        else:
            control.fbr = control.stack[control.sp-1]
            control.stack.pop()
            control.sp -= 1

def pushfbr(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        control.stack.append(control.fbr)
        control.sp += 1
#insertion
def pushimm(line, control):
    n = line[1].lstrip('-')
    if n.isdigit():
        control.sp += 1
        if line[1][0] == '-':
            control.stack.append(int(n) * -1)
        else:
            control.stack.append(int(n))
    else:
        print(f'Error in instruction "{line[0]}" expecting a number')
        control.halt = 1
        control.error = True

#insertion float
def pushimmf(line, control):
    n = line[1].lstrip('-')
    try:
        control.sp += 1
        if line[1][0] == '-':
            control.stack.append(float(n) * -1)
        else:
            control.stack.append(float(n))
    except:
        print(f'Error in instruction "{line[0]}" expecting a floating point number')
        control.halt = 1
        control.error = True
#addsp
def addsp(line, control):
    if len(line) < 2:
        print(f'Error in instruction "{line[0]}" too few arguments.')
        control.halt = 1
        control.error = True
        
    else: 
        n = line[1].lstrip('-')
        i = 0
        if n.isdigit():
            if line[1][0] == '-':
                for i in range(int(n)):
                    control.sp -= 1
                    if control.sp < 0:
                        print(f'Error in instruction "{line[0]}" SP cannot be negative.')
                        control.halt = 1
                        control.error = True
                    else:
                        control.pop()
            else:
                for i in range(int(n)):
                    control.sp += 1
                    control.stack.append(0)
            
        else:
            print(f'Error in instruction "{line[0]}" expecting a number')
            control.halt = 1
            control.error = True
    

def pushsp(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        control.stack.append(control.sp)
        control.sp += 1

def popsp(line, control):
    if len(line) > 1:
        print(f'Error in instruction "{line[0]}" too many arguments.')
        control.halt = 1
        control.error = True
    else:
        control.sp -= 1
        if control.sp < 0:
            print(f'Error in instruction "{line[0]}" SP cannot be negative.')
            control.halt = 1
            control.error = True
        else:
            control.sp = control.stack[control.sp]