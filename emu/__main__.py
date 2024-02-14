import yaml

from emu.bl import parse_yaml_data, parse_yaml_input, parse_yaml_instructions
from emu.soc import Soc

if __name__ == "__main__":

    with open("./output.yaml") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    data = parse_yaml_data(yaml_data["data"])
    instructions = parse_yaml_instructions(yaml_data["instructions"])
    buff = parse_yaml_input(yaml_data["input"])
    start_addr = int(yaml_data["start_addr"])

    soc = Soc()
    soc.run(start_addr, instructions, data, buff)

