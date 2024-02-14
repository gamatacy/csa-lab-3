from .isagenerator import add_halt, data, generator, get_start_point, instructions
from .parser import lisp_to_ast
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
