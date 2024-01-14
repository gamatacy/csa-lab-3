from hw import *
from alu import ALU

MEMORY_SIZE = 256

class DataPath:

    def __init__(self):

        #alu
        self.alu: ALU = ALU()

        #mem
        self.instructionMemory: Memory = Memory(MEMORY_SIZE)
        self.dataMemory: Memory = Memory(MEMORY_SIZE)

        #regs
        #lalu
        self.AC: Register = Register()
        self.BR: Register = Register()
        self.IR: Register = Register()
        self.IAR: Register = Register()

        #ralu
        self.DR: Register = Register()
        self.PS: Register = Register()
        self.SP: Register = Register()

        self.AR: Register = Register()

        self.mappedRegister: [Register] = [
                self.DR,
                self.SP,
                self.PS,
                self.AR,
                self.AC,
                self.BR,
                self.IAR
        ]
        
    def log_registers(self):

        print("======================")

        print("\nLEFT REGS:")
        print(f"   AC: {self.AC.getValue()}")
        print(f"   BR: {self.BR.getValue()}")
        print(f"   IR: {self.IR.getValue()}")
        print(f"   IAR: {self.IAR.getValue()}")

        print("\nRIGHT REGS:")
        print(f"   DR: {self.DR.getValue()}")
        print(f"   PS: {self.PS.getValue()}")
        print(f"   SP: {self.SP.getValue()}")
        print(f"   AR: {self.AR.getValue()}")

        print("\nDataMemory")
        for i in range(3):
            print(f"   ADDR: {i} VALUE: ", end="")
            print(f"{self.dataMemory.getValue(i)}")


