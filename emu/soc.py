from DataPath import DataPath, MEMORY_SIZE
from ControlUnit import ControlUnit
from instruction import Instruction


def run():
    dataPath = DataPath()
    controlUnit = ControlUnit()

    while (True):
        controlUnit.executeInstruction(
            dataPath.instructionMemory.getValue(
                dataPath.IAR.getValue()
            )
        )

        
    