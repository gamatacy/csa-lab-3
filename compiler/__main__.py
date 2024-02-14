from sys import argv

from yaml import dump

from compiler.compiler import compile_lisp

if __name__ == "__main__":
    input_file = open(argv[1])
    buff = ""
    if len(argv) > 3:
        buff = argv[3]

    yaml_data = compile_lisp(input_file, buff)

    with open(argv[2], "w") as output_file:
        dump(yaml_data, output_file, default_flow_style=False)




