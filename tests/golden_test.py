import logging
from io import StringIO

import pytest
from compiler.compiler import compile
from emu.bl import parse_yaml_data,parse_yaml_input,parse_yaml_instructions
from emu.soc import run

@pytest.mark.golden_test("golden/*.yaml")
def golden_test(golden, caplog, capsys, tmpdir):
    caplog.set_level(logging.DEBUG)
    log_formatter = logging.Formatter("%(message)s")
    caplog.handler.setFormatter(log_formatter)

    compiled_prog_buffer = StringIO()

    yaml_data = {}
    with open(golden["in_source"], encoding="utf-8") as code_source:
        yaml_data= compile(code_source, compiled_prog_buffer)

    data = parse_yaml_data(yaml_data['data'])
    instructions = parse_yaml_instructions(yaml_data['instructions'])
    buff = parse_yaml_input(yaml_data['input'])
    start_addr = int(yaml_data['start_addr'])
    
    run(start_addr, instructions, data, buff)

    expecteddump = open(golden["dump"], encoding="utf-8")
    realdump = open("emu.dump", encoding="utf-8")

    assert expecteddump.read() == realdump.read()
