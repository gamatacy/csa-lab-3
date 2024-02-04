from compiler.parser import lisp_to_ast
from compiler.isagenerator import *
from pprint import pprint


code = '''
((defun sum (a b) (
    (save a (+ a b))
    (ret a)
))
(_start_
    (let first (5))
    (let second (10))
    (call sum (first second))
)
)
'''
ast = lisp_to_ast(code)
pprint(ast)
generator(ast)
print("============")
for instr in instructions:
    print(f'{instr.instruction}: {instr.op}')
print("============")
for key, value in data.items():
    print(f"{key}: {value.addr}")
print("============")
print(get_start_point())
