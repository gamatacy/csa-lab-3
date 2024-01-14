from DataPath import DataPath, MEMORY_SIZE
from ControlUnit import ControlUnit
from instruction import *


def run():
    dataPath = DataPath()
    controlUnit = ControlUnit()

    dataPath.dataMemory.setValue(1,OpCode.HLT)

    print(
        OpCode(dataPath.dataMemory.getValue(1)).name
    )

    # while (True):
    #     controlUnit.executeInstruction(
    #         dataPath.instructionMemory.getValue(
    #             dataPath.IAR.getValue()
    #         )
    #     )

        
    