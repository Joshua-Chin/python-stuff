import subprocess
import os

def bf_to_c(src):
    code = ["#include <stdio.h>",
            "int main(){",
            "char array[30000] = {0};",
            "char* ptr = array;"]
    for char in src:
        if char == '>':
            code.append('++ptr;')
        elif char == '<':
            code.append('--ptr;')
        elif char == '+':
            code.append('++*ptr;')
        elif char == '-':
            code.append('--*ptr;')
        elif char == '.':
            code.append('putchar(*ptr);')
        elif char == ',':
            code.append('*ptr=getchar();')
        elif char == '[':
            code.append('while(*ptr){')
        elif char == ']':
            code.append('}')
    code.append('}')
    return "\n".join(code)

def compile_c(filename, new_filename=None):
    if new_filename is None:
        new_filename = filename.split('.')[0]
    subprocess.call(['clang', '-Ofast', '-o' + new_filename, filename])

def compile_bf(filename):
    with open(filename) as file:
        src = file.read()
    c_src = bf_to_c(src)
    c_filename = 'temp'+str(abs(hash(c_src)))+'.c'
    with open(c_filename, 'w') as file:
        file.write(c_src)
    compile_c(c_filename, filename.split('.')[0])
    os.remove(c_filename)

if __name__ == '__main__':
    import sys
    compile_bf(sys.argv[1])
