from emu.DataPath import DataPath
from emu.ControlUnit import ControlUnit


def run(start_addr: int, instructions: [int], data: [int], buffer: [int]):
    dataPath = DataPath()
    controlUnit = ControlUnit()

    dataPath.IAR.setValue(start_addr)
    dataPath.dataMemory.memory = data
    dataPath.instructionMemory.memory = instructions
    dataPath.buffers[735] = buffer

    controlUnit.runclk(dataPath)

    return