from emu.control_unit import ControlUnit
from emu.data_path import DataPath


class Soc:

    def __init__(self):
        pass

    def run(self, start_addr: int, instructions: [int], data: [int], buffer: [int]):
        data_path = DataPath()
        control_unit = ControlUnit()

        data_path.IAR.set_value(start_addr)
        data_path.dataMemory.memory = data
        data_path.instructionMemory.memory = instructions
        data_path.buffers[735] = buffer

        control_unit.runclk(data_path)
