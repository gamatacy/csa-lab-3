from DataPath import DataPath, MEMORY_SIZE
from ControlUnit import ControlUnit
from instruction import *


def run(start_addr: int, instructions: [int], data: [int], buffer: [int]):
    dataPath = DataPath()
    controlUnit = ControlUnit()

    dataPath.IAR.setValue(start_addr)
    dataPath.dataMemory.memory = data
    dataPath.instructionMemory.memory = instructions
    dataPath.buffers[735] = buffer

    controlUnit.runclk(dataPath)
