from DataPath import DataPath, MEMORY_SIZE
from ControlUnit import ControlUnit
from instruction import *


def run():
    dataPath = DataPath()
    controlUnit = ControlUnit()

    dataPath.instructionMemory.setValue(0, 1)
    dataPath.instructionMemory.setValue(1, 2)

    dataPath.dataMemory.setValue(0, 1337)
    
    while True:
        controlUnit.executeInstruction(
            dataPath,
            OpCodes[
                dataPath.instructionMemory.getValue(
                dataPath.IAR.getValue()
            )
            ]
        )

