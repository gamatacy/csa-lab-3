from hw import Memory
from DataPath import DataPath
from MicroCode import MicroCode
from instruction import Instruction

class ControlUnit:

    def executeInstruction(self, dataPath: DataPath, instruction: Instruction):
        
        mcodes: [int] = instruction.value

        for mcode in mcodes:
            if ( mcode & 0x80000000 ):
                jmpAddress: int | None = self.executeControlMicroCode(dataPath, mcode)

                if (type(jmpAddress) is not None):
                    pass

            else:
                self.executeOperationMicroCode(dataPath, mcode)


    def executeOperationMicroCode(self, dataPath: DataPath, mcode: int):
        self.executeMicroCode(dataPath, mcode)

        #save alu output to registers
        for offset in range(7):
            if ( mcode & ( 0x10000 << offset ) ):
                dataPath.mappedRegister[offset].setValue(dataPath.alu.getOutput())

        if ( mcode & 0x800000 ):
            dataPath.DR.setValue(
                dataPath.dataMemory.getValue(
                    dataPath.AR
                )
            )
        elif ( mcode & 0x1000000 ):
            dataPath.dataMemory.setValue(
                dataPath.AR.getValue(),
                dataPath.DR.getValue()
            )
        elif ( mcode & 0x2000000 ):
            pass
        elif ( mcode & 0x4000000 ):
            pass


    def executeControlMicroCode(self, dataPath: DataPath, mcode: int) -> int | None:
        self.executeMicroCode(dataPath, mcode)

        flagsMask:  int = mcode & 0xF0000 >> 16
        jmpAddress: int = mcode & 0xFF00000 >> 20

        aluFlags: int = dataPath.alu.getZ()
        aluFlags += (dataPath.alu.getN() << 1)
        aluFlags += (dataPath.alu.getC() << 2)
        aluFlags += (dataPath.alu.getV() << 3)

        if ( flagsMask == aluFlags ):
            return jmpAddress
        
        return None

    def executeMicroCode(dataPath: DataPath, mcode: int):
        
        #set right alu operand
        if   ( mcode & 0x1):
            dataPath.alu.setRightOperand(dataPath.DR)
        elif ( mcode & 0x2):
            dataPath.alu.setRightOperand(dataPath.SP)
        elif ( mcode & 0x4):
            dataPath.alu.setRightOperand(dataPath.PS)

        #set left alu operand
        if   ( mcode & 0x10):
            dataPath.alu.setLeftOperand(dataPath.AC)
        elif ( mcode & 0x20):
            dataPath.alu.setLeftOperand(dataPath.BR)
        elif ( mcode & 0x40):
            dataPath.alu.setLeftOperand(dataPath.IAR)
        elif ( mcode & 0x80):
            dataPath.alu.setLeftOperand(dataPath.IR)   

        #inverse operands
        if   ( mcode & 0x100 ):
            dataPath.alu.invLeftOperand()
        
        if   ( mcode & 0x200 ):
            dataPath.alu.invRightOperand()

        #sum/and
        if   ( mcode & 0x400 ):
            dataPath.alu.sum()
        elif ( mcode & 0x800 ):
            dataPath.alu.conjuction()

        #increment 
        if   ( mcode & 0x4000):
            dataPath.alu.inc()

        #shift
        if   ( mcode & 0x1000):
            dataPath.alu.shlt()
        elif ( mcode & 0x2000):
            dataPath.alu.shrt()

    
