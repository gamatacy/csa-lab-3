from compiler.parser import lisp_to_ast
from compiler.isagenerator import *
from pprint import pprint


# code = '''
# ((defun sum (a b) (
#     (save a (+ a b))
#     (ret a)
# ))
# (_start_
#     (let first (5))
#     (let second (10))
#     (call sum (first second))
# )
# )
# '''

code = '''
    (
    (let i (1))
    (let cond (1))
    (let value (10))
    (if (= i cond) (
        (save cond (1))
    ))
    (save i (value))
    )
'''

