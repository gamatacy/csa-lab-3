import logging
import pytest
from compiler.compiler import compile
from emu.bl import parse_yaml_data,parse_yaml_input,parse_yaml_instructions
from emu.soc import Soc

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
    
    soc = Soc()
    soc.run(start_addr, instructions, data, buff)

    a = open(golden["dump"],"r")
    b = open("emu.dump","r")

    assert a.read() == b.read()

    # assert filecmp.cmp(dump_name, "emu.dump")
