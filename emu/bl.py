from instruction import *

def parse_yaml_data(data_section: str):
    data = [0] * 2048
    for key, value in data_section.items():
        if isinstance(value['value'], int):
            data[value['addr']] = value['value']
        elif isinstance(value['value'], str):
            for char in value['value']:
                data[value['addr']] = ord(char)
                value['addr'] += 1
            value += chr(0)
    return data

def parse_yaml_instructions(instr_section):
    instructions = [0] * 50
    for idx, item in enumerate(instr_section):
        instruction = 0
        opcode = 0

        for k,v in OpCodes.items():
            if v == Instruction[item['instruction']]:
                opcode = k
                break

        instruction = ( 0x0000 | opcode ) << 24
        instruction |= item['op']

        instructions[idx] = instruction



    return instructions