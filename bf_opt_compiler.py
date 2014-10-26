from enum import Enum
from sympy import symbols, IndexedBase, Sum, pprint, Expr, decorators

class opcode(Enum):
    compute = 0
    shift = 1
    jump_if_0 = 2
    jump_if_not_0 = 3
    display = 4
    read = 5

#Separate assignment and increment
#Create general block class and loop clas, supporting add
class assign(Expr):

    def __init__(self, expr):
        self.expr = expr

    @decorators._sympifyit('other', NotImplemented)
    @decorators.call_highest_priority('__radd__')
    def __add__(self, other):
        if isinstance(other, assign):
            return other
        if isinstance(other, increment):
            return assign(self.expr+other.expr)
        return NotImplemented

    def __eq__(self, value):
        return isinstance(value, assign) and value.expr == self.expr
    
    def __repr__(self):
        return 'assign('+str(self.expr)+')'

class increment(Expr):

    def __init__(self, expr):
        self.expr = expr

    @decorators._sympifyit('other', NotImplemented)
    @decorators.call_highest_priority('__radd__')
    def __add__(self, other):
        if isinstance(other, assign):
            return other
        if isinstance(other, increment):
            return increment(self.expr+other.expr)
        return NotImplemented

    def __eq__(self, value):
        return isinstance(value, increment) and value.expr == self.expr
    
    def __repr__(self):
        return 'increment('+str(self.expr)+')'

class loop:

    def __init__(self, blocks):
        self.blocks = blocks

    def __repr__(self):
        return 'loop('+str(self.blocks)+')'

class block:

    def __init__(self, computations, shift, reads, writes):
        self.computations = computaitons
        self.shift = shift
        self.reads = reads
        self.writes = writes

    def __add__(self, value):
        if isinstance(value, block):
            pass
        return NotImplemented

    def __repr__(self):
        return 'block' + ", ".join(str(x) for x in [self.computations, self.shift, self.reads, self.writes])+')'

tape = IndexedBase('tape')
tape_index = symbols('tape_index')

def parse(src):
    """Parses the source code into blocks"""
    tree = [[]]
    
    for char in src:
        if char == '[':
            l = []
            tree[-1].append(l)
            tree.append(l)
        elif char == ']':
            tree.pop()
            
        elif char == '+':
            tree[-1].append((opcode.compute, tape_index, increment(1)))
        elif char == '-':
            tree[-1].append((opcode.compute, tape_index, increment(-1)))
        elif char == '>':
            tree[-1].append((opcode.shift, 1))
        elif char == '<':
            tree[-1].append((opcode.shift, -1))
        elif char == '.':
            tree[-1].append((opcode.display, tape_index))
        elif char == ',':
            tree[-1].append((opcode.read, tape_index))
    return tree[-1]

if __name__=='__main__':
    import pprint
    pprint.pprint(parse('++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'))
