from DataPath import DataPath, MEMORY_SIZE
from ControlUnit import ControlUnit
from instruction import *


def run():
    dataPath = DataPath()
    controlUnit = ControlUnit()

    loadInstructions(dataPath.instructionMemory.memory, [
        0x01010000,
        0x0F000735,
        0x02000000
    ])

    dataPath.dataMemory.setValue(0x0, 0x65)
    dataPath.dataMemory.setValue(0x1, 0x3)
    dataPath.dataMemory.setValue(0x2, 0x14)

    for addr, cell in enumerate(dataPath.instructionMemory.memory):
        print(f"ADDR: {hex(addr)}, INSTR: {hex(cell)}")
    
    controlUnit.runclk(dataPath)


def loadInstructions(memory: [int], rawInstructions: [int]):
    for addr, instruction in enumerate(rawInstructions):
        memory[addr] = instruction

