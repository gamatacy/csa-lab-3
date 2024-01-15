from DataPath import DataPath, MEMORY_SIZE
from ControlUnit import ControlUnit
from instruction import *


def run():
    dataPath = DataPath()
    controlUnit = ControlUnit()
    
    controlUnit.runclk(dataPath)


def loadInstructions(memory: [int], rawInstructions: [int]):
    for addr, instruction in enumerate(rawInstructions):
        memory[addr] = instruction

