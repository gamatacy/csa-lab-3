from hw import Memory
from typing import Optional
from DataPath import DataPath
from instruction import *
import sys

class ControlUnit:

    def __init__(self):
        self.tick = 0

    def runclk(self, dataPath: DataPath):
        instruction: Instruction
        rawInstruction: int

        while True:

            rawInstruction = dataPath.instructionMemory.getValue(
                dataPath.IAR.getValue()
            )

            dataPath.IR.setValue(rawInstruction)

            instruction = OpCodes[ ( rawInstruction >> 24 ) ]
            print()
            print(instruction)
            print()

            self.executeInstruction(dataPath, instruction)


    def executeInstruction(self, dataPath: DataPath, instruction: Instruction):

        if instruction is Instruction.NOP:
            print("NOP")
            sys.exit()

        if instruction is Instruction.HLT:
            print("HALT")
            sys.exit()

        mcodes: [int] = instruction.value

        for mcode in mcodes:

            if ( mcode & 0x80000000 ):
                if self.executeControlMicroCode(dataPath, mcode):
                    self.tick += 1
                    break
            else:
                self.executeOperationMicroCode(dataPath, mcode)
            
            print(f"TICK: {self.tick}")
            dataPath.log_registers()
            self.tick += 1


    def executeOperationMicroCode(self, dataPath: DataPath, mcode: int):
        self.executeMicroCode(dataPath, mcode)

        #save alu output to registers
        for offset in range(7):
            if ( mcode & ( 0x10000 << offset ) ):
                dataPath.mappedRegister[offset].setValue(dataPath.alu.getOutput())

        if ( mcode & 0x7800000 and (dataPath.IR.getValue() & 0x1FFFF) ):
            dataPath.AR.setValue(
                dataPath.IR.getValue() & 0xFFFF
            )

        if ( mcode & 0x800000 ):
            dataPath.DR.setValue(
                dataPath.dataMemory.getValue(
                    dataPath.AR.getValue()
                )
            )
        elif ( mcode & 0x1000000 ):
            dataPath.dataMemory.setValue(
                dataPath.AR.getValue(),
                dataPath.DR.getValue()
            )
        elif ( mcode & 0x2000000 ):
            dataPath.DR.setValue(
                dataPath.readBuffer(dataPath.AR.getValue())
            )
        elif ( mcode & 0x4000000 ):
            dataPath.writeBuffer(dataPath.AR.getValue(),
                dataPath.AC.getValue()
            )
            


    def executeControlMicroCode(self, dataPath: DataPath, mcode: int) -> bool:
        self.executeMicroCode(dataPath, mcode)

        flagsMask:  int = (mcode & 0xF0000) >> 16

        aluFlags: int = dataPath.getAcZ()
        aluFlags += (dataPath.getAcN() << 1)
        # aluFlags += (dataPath.alu.getC() << 2)
        # aluFlags += (dataPath.alu.getV() << 3)

        if ( flagsMask & aluFlags ):
            
            dataPath.IAR.setValue(
                dataPath.IR.getValue() & 0x1FFFF
            )
            dataPath.log_registers()
            return True
        
        return False
    

    def executeMicroCode(self, dataPath: DataPath, mcode: int):
        #clear alu
        dataPath.alu.setLeftOperand(0)
        dataPath.alu.setRightOperand(0)

        #set right alu operand
        if   ( mcode & 0x1):
            dataPath.alu.setRightOperand(dataPath.DR.getValue())
        elif ( mcode & 0x2):
            dataPath.alu.setRightOperand(dataPath.SP.getValue())
        elif ( mcode & 0x4):
            dataPath.alu.setRightOperand(dataPath.PS.getValue())

        #set left alu operand
        if   ( mcode & 0x10):
            dataPath.alu.setLeftOperand(dataPath.AC.getValue())
        elif ( mcode & 0x20):
            dataPath.alu.setLeftOperand(dataPath.BR.getValue())
        elif ( mcode & 0x40):
            dataPath.alu.setLeftOperand(dataPath.IAR.getValue())
        elif ( mcode & 0x80):
            dataPath.alu.setLeftOperand(dataPath.IR.getValue())   

        #inverse operands
        if   ( mcode & 0x200 ):
            dataPath.alu.invLeftOperand()
        
        if   ( mcode & 0x100 ):
            dataPath.alu.invRightOperand()

        #sum/and
        if   ( mcode & 0x400 ):
            dataPath.alu.sum()
        elif ( mcode & 0x800 ):
            dataPath.alu.conjuction()

        #increment 
        if   ( mcode & 0x4000 ):
            dataPath.alu.inc()

        #only 2 lower bytes 
        if   ( mcode & 0x8000 ):
            dataPath.alu._2lb()

        #shift
        if   ( mcode & 0x1000 ):
            dataPath.alu.shlt()
        elif ( mcode & 0x2000 ):
            dataPath.alu.shrt()

    
