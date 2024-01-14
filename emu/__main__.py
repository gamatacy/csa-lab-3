from DataPath import DataPath
from ControlUnit import ControlUnit
from instruction import Instruction

if __name__ == "__main__":
    dataPath = DataPath()
    controlUnit = ControlUnit()

    dataPath.dataMemory.setValue(0, 228)

    controlUnit.executeInstruction(dataPath,Instruction.LD)