import logging
import pytest
from compiler.compiler import compile
from emu.bl import parse_yaml_data,parse_yaml_input,parse_yaml_instructions
from emu.soc import Soc
import filecmp

@pytest.mark.golden_test("golden/*.yaml")
def test_golden(golden, caplog):
    caplog.set_level(logging.DEBUG)
    log_formatter = logging.Formatter("%(message)s")
    caplog.handler.setFormatter(log_formatter)

    yaml_data = {}
    with open(golden["in_source"], encoding="utf-8") as code_source:
          try: 
            buff = golden["input"]
          except:
            buff = []
          yaml_data= compile(code_source, buff)
    

    data = parse_yaml_data(yaml_data['data'])
    instructions = parse_yaml_instructions(yaml_data['instructions'])
    buff = parse_yaml_input(yaml_data['input'])
    start_addr = int(yaml_data['start_addr'])
    
    dump_name = golden["dump"]
    idx = 0
    f = open(dump_name, "r")
    for line in f.readlines():
        print(line)
        idx += 1
        if (idx == 15): break

    soc = Soc()
    soc.run(start_addr, instructions, data, buff)

    assert filecmp.cmp(dump_name, "emu.dump")
