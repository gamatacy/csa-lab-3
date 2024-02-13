from .parser import *
from .isagenerator import *
from .preprocessor import parse_includes
from sys import argv
from yaml import dump
import compiler

if __name__ == "__main__":
    input_file = open(argv[1], "r")
    input = ""
    if len(argv) > 3:
        input = argv[3]

    yaml_data = compile(input_file, input)

    with open(argv[2], "w") as output_file:
        dump(yaml_data, output_file, default_flow_style=False)
    
    

    
