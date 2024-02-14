from emu.сontrolUnit import ControlUnit
from emu.dataPath import DataPath


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
