from sys import argv

from yaml import dump

from compiler.compiler import compile

if __name__ == "__main__":
    input_file = open(argv[1])
    input = ""
    if len(argv) > 3:
        input = argv[3]

    yaml_data = compile(input_file, input)

    with open(argv[2], "w") as output_file:
        dump(yaml_data, output_file, default_flow_style=False)




