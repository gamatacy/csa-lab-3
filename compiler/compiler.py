from .parser import lisp_to_ast
from .isagenerator import generator, add_halt,get_start_point, data, instructions
from .preprocessor import parse_includes


def compile(input_file,buffer=""):
     
    code = input_file.read()
    code = parse_includes(code)

    ast = lisp_to_ast(code)
    generator(ast)
    add_halt()
    iar = get_start_point()

    input = buffer

    yaml_data = {
        "start_addr" : iar,
        "instructions": [{"instruction": inst.instruction.name,"op": inst.op, "addr" : hex(idx)} for idx, inst in enumerate(instructions)],
        "data" : {key: value.__dict__ for key, value in data.items()},
        "input" : input 
        }
    
    return yaml_data