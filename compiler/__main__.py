from .parser import *
from .isagenerator import *
from .preprocessor import parse_includes
from sys import argv
from yaml import dump

if __name__ == "__main__":
    print(argv[1])
    input_file = open(argv[1], "r")
    
    code = input_file.read()
    code = parse_includes(code)

    print(code)

    ast = lisp_to_ast(code)
    generator(ast)
    add_halt()

    yaml_data = {
         "instructions": [{"instruction": inst.instruction.name, "op": inst.op} for inst in instructions],
        "data": {key: value.__dict__ for key, value in data.items()}
        }

    with open(argv[2], "w") as output_file:
        dump(yaml_data, output_file, default_flow_style=False)
    
    iar = get_start_point()

    
