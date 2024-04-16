class Program:
    def __init__(self):
        self.halt = 0
        self.sp = 0
        self.fbr = 0
        self.pc = 0
        self.length = 0
        self.stack = []
        self.labels = {}
    
    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        else:
            print(f'Processor Error: Stack Underflow at instruction {self.pc}.')
            exit(1)
        